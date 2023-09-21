import torch
import torch.nn.functional as F
#ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import torch
import torch.nn.functional as F
from concurrent.futures import ThreadPoolExecutor
from numpy import roll


def roll(data,shift):
    assert data.shape[0] == shift.shape[0]
    shift = shift-shift.min()
    re = np.zeros_like(data)
    for i in range(data.shape[0]):
        re[i] = np.roll(data[i],shift[i],axis=0)
    return re

def tmf(tmp, data, step=1, device='cpu', moves=[], batch_size=-1, save_memory=False, max_workers=4):
    """
    Calculates the cross-correlation between a template and an image using convolution.

    Args:
        tmp (numpy.ndarray or torch.Tensor): The template to be matched.
        data (numpy.ndarray or torch.Tensor): The image to search for the template.
        step (int, optional): The step size of the convolution. Defaults to 1.
        device (str, optional): The device to perform the computation on. Defaults to 'cpu'.
        moves (list, optional): A list of moves to apply to the template before matching. Defaults to [].
        batch_size (int, optional): The batch size to use for the computation. Defaults to -1.
        save_memory (bool, optional): Whether to use half-precision floating point numbers to save memory. Defaults to False.
        max_workers (int, optional): The maximum number of worker threads to use for the computation. Defaults to 4.

    Returns:
        numpy.ndarray: The cross-correlation between the template and the image.
    """
    if batch_size == -1:
        batch_size = data.shape[0]
    if moves != []:
        # if the moves is not a numpy.ndarray, convert it to numpy.ndarray
        if not isinstance(moves,np.ndarray):
            moves = np.array(moves)
        moveout = [moves[:,i] for i in range(0,moves.shape[1],batch_size)]
        moveout = np.array(moveout).T
    else:
        moveout = []
    # if data is not torch.tensor type, convert it to torch.tensor type
    if not isinstance(data,torch.Tensor):
        data = torch.from_numpy(data)
    # if tmp is not torch.tensor type, convert it to torch.tensor type
    if not isinstance(tmp,torch.Tensor):
        tmp = torch.from_numpy(tmp)
    # if data is not float type, convert it to float type
    if data.dtype != torch.float:
        data = data.float()
    # if tmp is not float type, convert it to float type
    if tmp.dtype != torch.float:
        tmp = tmp.float()
    if save_memory:
        data = data.half()
        tmp = tmp.half()
    else:
        # if data is not on device, move it to device
        if data.device != device:
            data = data.to(device)
        # if tmp is not on device, move it to device
        if tmp.device != device:
            tmp = tmp.to(device)
    # tmp: [tmp_num, height, tmp_width]
    # data: [data_height, data_width]
    data_shape = data.shape
    tmp_shape = tmp.shape
    assert len(data_shape) == 2
    assert len(tmp_shape) == 3
    assert tmp_shape[1] == data_shape[0]
    assert tmp_shape[2] <= data_shape[1]
    assert step > 0
    assert moveout == [] or len(moveout) == tmp_shape[0]
    assert data_shape[0] > 0 and data_shape[1] > 0
    tmp_num = tmp_shape[0]
    height = tmp_shape[1]
    tmp_width = tmp_shape[2]
    data_height, data_width = data_shape[0], data_shape[1]
    if device == 'cpu':
        #考虑step
        ans_width = (data_width - tmp_width) // step + 1
        corr_all = np.zeros((tmp_num,data_height//batch_size,ans_width))
        def cal_corr(i):
            tmp_data = data[i:i + batch_size, :].sum(axis=0).view(1,1,data_width)
            tmp_tmp = tmp[:, i:i + batch_size, :].sum(axis=1,keepdims=True)
            #print(tmp_data.shape,tmp_tmp.shape)
            corr = F.conv1d(tmp_data, tmp_tmp, stride=step)
            nor1 = F.conv1d(tmp_data ** 2, torch.ones_like(tmp_tmp), stride=step)
            nor_tmp = (tmp_tmp ** 2).sum(dim=(1, 2)).unsqueeze(1)
            corr = corr / torch.sqrt(nor1 * nor_tmp)
            corr_all[:,i,:] = corr.numpy()
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(cal_corr,range(0,data_height,batch_size))
    else:
        corr_all = []
        for i in range(0, data_height, batch_size):
            tmp_data = data[i:i + batch_size, :].sum(axis=0).view(1,1,data_width)
            tmp_tmp = tmp[:, i:i + batch_size, :].sum(axis=1,keepdims=True)
            corr = F.conv1d(tmp_data, tmp_tmp, stride=step).cpu()
            nor1 = F.conv1d(tmp_data ** 2, torch.ones_like(tmp_tmp), stride=step).cpu()
            nor_tmp = (tmp_tmp ** 2).sum(dim=(1, 2)).unsqueeze(1).cpu()
            # "sqrt_vml_cpu" not implemented for 'Half'
            corr = corr.float()
            nor1 = nor1.float()
            nor_tmp = nor_tmp.float()
            corr = corr / torch.sqrt(nor1 * nor_tmp)
            corr_all.append(corr.cpu().numpy())
        corr_all = np.stack(corr_all,axis=1)
    if moveout != []:
        for i in range(tmp_num):
            move = moveout[i]-moveout[i].min()
            move = move.astype(int)
            move = move//step
            corr_all[i] = roll(corr_all[i],move[::-1])
    return corr_all


