# Tech_Hustlers2.0-Blockcam
![blockcam](https://github.com/user-attachments/assets/023ec62b-9c7d-4a48-b111-772efb8af52e)

Smart Contract - 0xdc80893e98432b457c85936dead2ad2fbd7b3b40156d3f70acb8993ddc057fb9

PROJECT TITLE:
Blockcam smart contract on Aptos Blockchain

Project Description:
The BlockCam Smart Contract is a decentralized application (dApp) built using the Move programming language and deployed on the Aptos blockchain.BlockCam is an innovative security solution that leverages blockchain technology to secure and audit CCTV footage. By employing an immutable ledger, BlockCam ensures the integrity of video data, making it resistant to tampering and unauthorized access. This solution is ideal for organizations that require reliable and verifiable surveillance records, offering a higher level of trust and transparency in video monitoring systems.

Project visuals:
~login page
![blockcam1](https://github.com/user-attachments/assets/7d573193-2dd4-43aa-91f2-ae51f74e450b)
~connecting wallet
![blockcam2](https://github.com/user-attachments/assets/42f1250d-cd81-45a6-a1f1-8dfb7dca5fc6)
~wallet address retrieved
![blockcam3](https://github.com/user-attachments/assets/25013ee1-27a9-4828-bbfc-a32a470803a0)
~functions page
![blockcam4](https://github.com/user-attachments/assets/582b89f8-148b-4cd3-8aaa-cca8c5714e7a)

Key Features:
~Blockchain Security:
Securely stores CCTV footage on a tamper-proof blockchain.
~Immutable Ledger:
Creates an unchangeable audit trail with time-stamped, cryptographically hashed footage.
~Integrated Functions: 
Functions like retrieving footage, checking wallet balance and deposit tokens to the wallet 
~Scalable Integration:
Compatible with existing CCTV systems; supports various camera types and formats.
~Access Control:Restricts access using cryptographic keys; supports role-based permissions.

The Tech and Tools used:
~Move Programming Language & Web3
~Petra Crypto Wallet 
~Aptos-SDK to develop the smart-contract
~Aptos Blockchain (Testnet)
~remix.ethereum.org (for writting and testing the smart contract)
~React.JS to build the frontend

Road Map/Project Vision:
BlockCam aims to revolutionize the security industry by introducing an unparalleled level of trust and integrity into CCTV surveillance. By leveraging the power of blockchain, BlockCam not only secures video footage but also enhances transparency and accountability in security operations. Our vision is to establish BlockCam as the gold standard for surveillance systems in industries where data integrity is critical, such as law enforcement, financial institutions, and public infrastructure. We aspire to create a world where video evidence is not only secure but also indisputable, empowering organizations to protect their assets and ensure public safety with confidence.

Software Development Plan for Blockcam dApp on Stellar Blockchain:


Smart Contract Functions and Variables
Develop the smart contract to include key functions:

add_footage(owner : address, ipfs_hash : String): It adds the hash of the video at footages vector of the owner address.
get_vault_address(admin_address : address): Allow users to get the get the address of the wallet.
deposit_tokens(admin : &signer, amount : u64): Allow the users to deposit tokens to their account.
get_footage_count(account: address): Allow users to get total footage count of their cams
get_footage(account: address, index: u64): Allow users to get footage of a particular index from the footage vector.
vault_balance(admin_address : address): Allow users to the balance of their wallet at our site.

Define essential variables:
struct Footage : It will have the ipfs_hash and timestamp of the footages.
struct Footage : Stores the ipfs_hash and timestamp of the footages.
struct SurveillanceData : Stores the footages and address of the owner.
struct Vault : Stores the admin address, vault address and balance of the vault.
struct VaultSignerCapability : Stores the capability of the vault to the owner