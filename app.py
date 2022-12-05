# -*- coding: utf-8 -*-


from flask import Flask, request, render_template
import joblib
from sklearn.preprocessing import Normalizer
app = Flask(__name__)

import pickle, joblib
# model_save_name =r"C:\Users\NaumanRafique\Downloads\Yashil\model.pkl"
vector_save_name = r"C:\Users\NaumanRafique\Downloads\Yashil\vector.pkl"
vectorizer = pickle.load(open(vector_save_name, 'rb'))
# message = "dear emad trust email find well receive attached form tcc refund deducted tax amount please fill send back u asap best regard mesfer smesfer srmanager text 171 f 96614168989 966558281100 e user domain com email file transmitted may confidential intended solely use addressed individual entityreceived email error kindly notify sender immediately disclose content person store copy information mediumsignatory tcc accepts liability damage caused virus transmitted emailtcc email file transmitted may confidential intended solely use addressed individual entityto person store copy information mediumemail view opinion presented email solely author necessarily represent tcc email file transmitted may confidential intended solely use addressed individual entityto person store copy information mediumemail view opinion presented email solely author necessarily represent tcc email file transmitted may confidential intended solely use addressed individual entityto person store copy information mediumemail view opinion presented email solely author necessarily represent tcc email file transmitted may confidential intended solely use addressed individual entityto person store copy information mediumemail view opinion presented email solely author necessarily represent tcc"

# vec = vectorizer.transform([message]).toarray()
# print(len(vec.toarray()[0]))

# with open(model_save_name, 'rb') as f:
#     model_rnn = pickle.Unpickler(f)

# model_rnn = pickle.load(open(model_save_name, 'rb'))


@app.route('/')
def home():
    # print(np.__version__)
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def predict():
    message = []
    for m in  request.form.values():
        message.append(m)
    # # message = message.strip()
    # print(message.)
    # message = "My name is nomi123123123"
    print(message)
    vec = vectorizer.transform(message).toarray()
    # output = vec
    # output = model_rnn.predict(vec.toarray().reshape(1, 200, 20))
    # print(vec)
    # if output.index(max(output)):
    #     message = "Given Email is Phihing"
    # else:
    #     message = "Given Email is Legit"

    # input_features = [int(x) for x in request.form.values() if type(x)==]
    # features_value = np.array(input_features)
    
    #validate input hours
    # if input_features[0] <0 or input_features[0] >24:
    #     return render_template('form.html', prediction_text='Please enter valid hours between 1 to 24 if you live on the Earth')
    #
    #
    # output = model.predict([features_value])[0][0].round(2)

    # input and predicted value store in df then save in csv file
    # df= pd.concat([df,pd.DataFrame({'Study Hours':input_features,'Predicted Output':[output]})],ignore_index=True)
    # print(df)
    # df.to_csv('smp_data_from_app.csv')

    return render_template('index.html',items= message)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)

    