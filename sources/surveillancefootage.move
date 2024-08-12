module cctv::surveillancefootage {
    use std::signer;
    use std::string::String;
    use aptos_framework::coin;
    use aptos_framework::aptos_coin::AptosCoin;
    use aptos_framework::account;
    use std::vector;
    use aptos_framework::timestamp;

    const E_NO_OWNER : u64 = 0 ;
    const E_NOT_OWNER : u64 = 1 ;
    const E_NOT_ADMIN : u64 = 2;

    struct Footage has copy, drop, store {
        ipfs_hash: String,
        timestamp: u64,
    }

    struct SurveillanceData has key {
        footages: vector<Footage>,
        owner: address,
    }

    struct Vault has key{
        admin : address,
        vault_address : address,
        total_balance : u64,
    }
    struct VaultSignerCapability has key{
        cap : account::SignerCapability
    }

    fun init_module(account: &signer) {
        let owner = signer::address_of(account);
        assert!(!exists<SurveillanceData>(owner), E_NO_OWNER);
        let (vault_signer, vault_signer_cap) = account::create_resource_account(account, b"Vault");
        let vault_address = signer::address_of(&vault_signer);
        if(!coin::is_account_registered<AptosCoin>(vault_address)){
        coin::register<AptosCoin>(&vault_signer);
    };

        let data = SurveillanceData {
            footages: vector::empty<Footage>(),
            owner: owner,
        };
        

        move_to(&vault_signer, Vault{
        admin : owner,
        vault_address,
        total_balance : 0,
        
    });
    
        move_to(account, data);
        move_to(account, VaultSignerCapability{
        cap : vault_signer_cap,
    });
    }
    #[view]
    public fun get_vault_address(admin_address : address): address acquires VaultSignerCapability{
        let vault_signer_cap = &borrow_global<VaultSignerCapability>(admin_address).cap;
        account::get_signer_capability_address(vault_signer_cap)
    }

    public entry fun deposit_tokens(admin : &signer, amount : u64) acquires Vault, VaultSignerCapability{
        let admin_address = signer::address_of(admin);
        let vault_address = get_vault_address(admin_address);
        let vault = borrow_global_mut<Vault>(vault_address);
        assert!(vault.admin == signer::address_of(admin), E_NOT_ADMIN);
        coin::transfer<AptosCoin>(admin, vault_address, amount);
        vault.total_balance = vault.total_balance + amount;
    }

    public entry fun add_footage(owner: address, ipfs_hash: String) acquires SurveillanceData{
        let data = borrow_global_mut<SurveillanceData>(owner);
        assert!(data.owner == owner, E_NOT_OWNER);
        let current_time = timestamp::now_seconds();
        let footage = Footage {
            ipfs_hash: ipfs_hash,
            timestamp: current_time,
        };
        vector::push_back(&mut data.footages, footage);
    }
    #[view]
    public fun get_footage_count(account: address): u64 acquires SurveillanceData {
        let data = borrow_global<SurveillanceData>(account);
        vector::length(&data.footages)
    }
    public  fun get_footage(account: address, index: u64): String acquires SurveillanceData {
        let data = borrow_global<SurveillanceData>(account);
        let footage = vector::borrow(&data.footages, index);
        footage.ipfs_hash
    }
    #[view]
    public fun vault_balance(admin_address : address) : u64 acquires Vault, VaultSignerCapability{
        let vault_address = get_vault_address(admin_address);
        let vault = borrow_global<Vault>(vault_address);
        vault.total_balance
    }


}
