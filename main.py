from flask import Flask, render_template, request, jsonify
from flask_talisman import Talisman
from flask_cors import CORS
import requests  as req
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

CORS(app)

# Talisman(app)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/api/get_preview', methods=['POST'])
def get_preview():

    url = request.json['targeturl']

    blocked_domains = [
    'localhost', 'localhost.', '127.0.0.1', '0.0.0.0', '127.1', '127.0.1',
    
    '[::1]', '[::]', '[0:0:0:0:0:0:0:1]', '[::ffff:127.0.0.1]',
    
    'localtest.me', 'lvh.me', 'localh.st', 'vcap.me', 'alias.com', 
    'lacolhost.com', 'icann.org', 'bit.ly',
    
    'nip.io', 'sslip.io', 'customer-127-0-0-1.aesir.cloud',
    
    '169.254.169.254', 'instance-data', 'metadata.google.internal', 
    'metadata.tencentyun.com', '100.100.100.200',
    
    '2130706433',
    '0x7f000001',   
    '0177.000.000.001', 
    
    'oastify', 'oast.me', 'oast.live', 'oast.pro', 'oast.fun',
    'burpcollaborator.net', 'interact.sh', 'interactsh.com',
    'webhook.site', 'requestbin.net', 'requestbin.com', 
    'pipedream.net', 'beeceptor.com', 'requestcatcher.com'
]

    for blacklisted_domain in blocked_domains:
        if "Sup3rS3cr37C0d3!!" in url:

            flag = {
                'flag': 'flag{ssrf_1s_c001}'
            }
            req.get(url, json=flag)
            return jsonify({
        "body_html": "Check your server"
    })

        if blacklisted_domain in url:
            print(blacklisted_domain)
            return jsonify({
        "body_html": "Haha, nice try. I can still read it."
    })  

    response = req.get(url)

    body_html = response.text


    return jsonify({
        "body_html": body_html
    })
    

@app.route('/verify', methods=["POST"])
def verify_flag():
    flag = request.json['flag']

    if flag == "flag{ssrf_1s_c001}":
        return jsonify({
        "body_html": 'Successfuly solved the lab!'
    })

    else:
        return jsonify({
        "body_html": 'Incorrect flag!'
    })


if __name__ == "__main__":
    app.run(debug=True)
