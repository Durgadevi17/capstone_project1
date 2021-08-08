from data_preprocessing import preprocessor

def classify_message(model,message):
    message = preprocessor(message)
    label = model.predict([message])[0]
    return {"label": label}
    