
import tensorflow as tf


path_model = 'app/models'

def get_prediction(data):    
    loaded = tf.saved_model.load(path_model)    
    res = loaded([data])
    tensor_data = res[1].numpy()
    json_data = {
        "dtype": str(tensor_data.dtype),
        "shape": tensor_data.shape,
        "data": tensor_data.tolist(),
    }
    res = json_data["data"]
    return res
