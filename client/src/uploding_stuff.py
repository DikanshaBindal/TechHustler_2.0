import ffmpeg
import os
import time
from pinatapy import PinataPy
import requests
import json
import hashlib
from nacl.signing import SigningKey
from nacl.encoding import HexEncoder

# Pinata API credentials
pinata_api_key = '58367924f34f7ac1fe18'
pinata_secret_api_key = 'a3d830f7757f1d86a9b560887b15967ed9f373cc361edc756faa3534305c5306'

# Aptos account credentials
private_key_hex = '0x2f7884447df76e921b37f0b46986c01b8707fab1d5c7e4063ec97b9382f56339'
node_url = 'https://fullnode.devnet.aptoslabs.com/v1'  # Adjust if using Testnet or Mainnet

# Initialize Pinata client
pinata = PinataPy(pinata_api_key, pinata_secret_api_key)

# Initialize Aptos account
signing_key = SigningKey(private_key_hex, encoder=HexEncoder)
public_key = signing_key.verify_key.encode(encoder=HexEncoder).decode('utf-8')
address = '0x' + hashlib.sha3_256(signing_key.verify_key.encode()).hexdigest()

# Function to encode video to H.264
def encode_video(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(output_file, vcodec='libx264').run(overwrite_output=True)
        print(f'Encoded {input_file} to {output_file}')
    except ffmpeg.Error as e:
        print(f'Error encoding video: {e}')
        return None

# Function to upload file to IPFS via Pinata
def upload_to_ipfs(file_path):
    response = pinata.pin_file_to_ipfs(file_path)
    return response['IpfsHash']

# Function to create and submit a transaction to Aptos blockchain
def create_aptos_transaction(recipient_address, amount, ipfs_hash):
    sequence_number = get_sequence_number(address)
    payload = {
        "type": "entry_function_payload",
        "function": "0x1::your_contract_module::store_ipfs_hash",  # Replace with your function
        "type_arguments": [],
        "arguments": [recipient_address, str(amount), ipfs_hash]
    }
    transaction = {
        "sender": address,
        "sequence_number": str(sequence_number),
        "max_gas_amount": "1000",
        "gas_unit_price": "1",
        "expiration_timestamp_secs": str(int(time.time()) + 600),
        "payload": payload
    }
    signed_transaction = sign_transaction(transaction)
    submit_transaction(signed_transaction)

# Function to get the sequence number for the account
def get_sequence_number(account_address):
    response = requests.get(f'{node_url}/accounts/{account_address}')
    return int(response.json()['sequence_number'])

# Function to sign the transaction
def sign_transaction(transaction):
    txn_bytes = json.dumps(transaction).encode('utf-8')
    signed_txn = signing_key.sign(txn_bytes).signature.hex()
    transaction['signature'] = {
        "type": "ed25519_signature",
        "public_key": public_key,
        "signature": signed_txn
    }
    return transaction

# Function to submit the transaction to the Aptos blockchain
def submit_transaction(transaction):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'{node_url}/transactions', headers=headers, data=json.dumps(transaction))
    if response.status_code == 202:
        print('Transaction submitted successfully.')
    else:
        print(f'Error submitting transaction: {response.json()}')

# Example continuous loop for encoding videos, uploading to IPFS, and creating transactions
def continuous_video_processing(directory_path, recipient_address, amount):
    while True:
        for file_name in os.listdir(directory_path):
            input_file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(input_file_path):
                # Define the output file name
                output_file_name = f'encoded_{file_name}'
                output_file_path = os.path.join(directory_path, output_file_name)

                # Encode the video
                encode_video(input_file_path, output_file_path)

                # Upload to IPFS
                ipfs_hash = upload_to_ipfs(output_file_path)
                print(f'Uploaded {output_file_name} to IPFS with hash {ipfs_hash}')

                # Create and submit transaction
                create_aptos_transaction(recipient_address, amount, ipfs_hash)
                print(f'Transaction created for {output_file_name} with IPFS hash {ipfs_hash}')

                # Optionally, delete or move the processed files
                os.remove(input_file_path)
                os.remove(output_file_path)
                
        # Add a delay if necessary
        time.sleep(10)

# Main execution
if __name__ == "__main__":
    directory_path = 'path_to_your_video_directory'  # Directory to monitor for new video files
    recipient_address = 'recipient_address'          # Address to send the transaction to
    amount = 1000000                                 # Amount to send (in smallest unit)

    continuous_video_processing(directory_path, recipient_address, amount)
