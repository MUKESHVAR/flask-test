from flask import Flask,request,jsonify

main = Flask(__name__)

@main.route('/')
def index():
    return "Hello world"

@main.route('/predict',methods=['POST'])
def predict():
    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')

    input_query = np.array([[cgpa,iq,profile_score]])

    result = {'cgpa':cgpa,'iq':iq,'profile_score':profile_score}

    return jsonify(result)

if __name__ == '__main__':
    main.run(debug=True)
