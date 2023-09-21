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

def tmf(tmp,data,step=1,device='cpu',moves=[],batch_size=-1,save_memory=False,max_workers=4,is_sum=False):
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
        max_workers (int, optional): 
            The maximum number of worker threads to use for the computation. Defaults to 4.
            notice: Considering Torch's multithreading, max_workers here do little work.
        is_sum (bool, optional): Whether to sum the cross-correlation along the height axis. Defaults to False.

    Returns:
        numpy.ndarray: The cross-correlation between the template and the image.
    """
    if batch_size == -1:
        batch_size = data.shape[0]
    if moves != []:
    # 如果moveout不是numpy类型，转换为numpy类型
        if not isinstance(moves,np.ndarray):
            moves = np.array(moves)
        moveout = [moves[:,i] for i in range(0,moves.shape[1],batch_size)]
        moveout = np.array(moveout).T
    else:
        moveout = []
    # 如果data不是torch.tensor类型，转换为torch.tensor类型
    if not isinstance(data,torch.Tensor):
        data = torch.from_numpy(data)
    # 如果tmp不是torch.tensor类型，转换为torch.tensor类型
    if not isinstance(tmp,torch.Tensor):
        tmp = torch.from_numpy(tmp)
    #print(tmp.shape,tmp.ndim)
    if tmp.ndim == 2:
        tmp = tmp.unsqueeze(0)
    # 如果data不是float类型，转换为float类型
    if data.dtype != torch.float:
        data = data.float()
    # 如果tmp不是float类型，转换为float类型
    if tmp.dtype != torch.float:
        tmp = tmp.float()
    if save_memory:
        data = data.half()
        tmp = tmp.half()
    else:
        # 如果data不在device上，转换到device上
        if data.device != device:
            data = data.to(device)
        # 如果tmp不在device上，转换到device上
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
        print(corr.shape)
        corr_all = np.vstack(corr_all)
        corr_all = np.swapaxes(corr_all,0,1)


    if moveout != []:
        for i in range(tmp_num):
            move = moveout[i]-moveout[i].min()
            move = move.astype(int)
            move = move//step
            corr_all[i] = roll(corr_all[i],move[::-1])
    if is_sum:
        corr_all = corr_all.sum(axis=1)
    return corr_all



