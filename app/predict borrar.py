import tensorflow as tf

#pred[m["asin"].numpy()] = model.RankingModel()(tf.convert_to_tensor([data]),tf.convert_to_tensor([m["asin"]]))

# def get_prediction(model, data):
#     pred = {}
#     x = model.ranking_model
#     for m in range(6):   
#         pred[m["asin"].numpy()] = x(tf.convert_to_tensor([data]),tf.convert_to_tensor([m["asin"]]))

#     return  sorted(pred, key=pred.get, reverse=True)

def get_prediction(model, data):
    return  model(data)