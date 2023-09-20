from numpy import load
from numpy import ndarray
from os.path import join
from torch import device
from torch.cuda import is_available
from numpy import min as min_, max as max_
from numpy import mean  as mean_,std as std_
from torch import from_numpy

def _tensor_or_ndarray(data, dtype="ndarray"):
    _data = data
    if dtype == "ndarray":
        if type(_data) == ndarray:
            return _data
        else:
            return _data.numpy()
    if dtype=="tensor":
        if type(_data) == ndarray:
            return from_numpy(_data)
        else:
            return _data

if __name__ == "__main__":
    from numpy import array
    data = _tensor_or_ndarray(array([[1, 2, 3], [3, 4, 5]]), "tensor")
    print(type(data), data)



def min_max(data, dtype="ndarray"):
    min_data, max_data = min_(data),max_(data)
    _data = (data - min_data)/(max_data-min_data)
    return _tensor_or_ndarray(_data, dtype=dtype)
    # if dtype == "ndarray":
    #     if type(_data) == ndarray:
    #         return _data
    #     else:
    #         return _data.numpy()
    # if dtype=="tensor":
    #     if type(_data) == ndarray:
    #         return from_numpy(_data)
    #     else:
    #         return _data
    # return _data
def standardization(data, dtype="ndarray"):
    mu = mean_(data, axis=0)
    sigma = std_(data, axis=0)
    return _tensor_or_ndarray((data - mu) / sigma, dtype=dtype)

def get_device(gpu_index=0):
    d = str( device("cuda:"+str(gpu_index) if is_available() else "cpu"))
    if ('cpu' == d):
        print("CPU MODE")
    return device("cuda:"+str(gpu_index) if is_available() else "cpu")

print(type(str(get_device())))

from os.path import dirname

def get_vol6(nums: int, type = 64, dtype="ndarray"):
    '''
    获得一个64个序列长度的电池电压第6阶段放电数据
    '''
    # import sys
    # dir_path = abspath('tool.py')
    # print(sys.path[0])
    # chdir(dir_path[0])
    dir_name = dirname(__file__)
    # real_path = join(dir_name,'vol6_64.py')
    real_path = None
    real_path = join(dir_name, 'vol6_64.py')
    if type == 75:
        real_path = join(dir_name,'vol50000.py')

    # abs_path = abspath('tool.py')
    # print(abs_path)
    data = load(real_path)
    if nums > data.shape[0]:
        print('Warning: max size is ', data.shape[0])
    return _tensor_or_ndarray(data[0:nums], dtype=dtype)


# x = np.zeros((100, 100))

# print(x.shape)
# print(x[0:1010].shape)

# get_vol6_64(10221)