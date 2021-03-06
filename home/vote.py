import json
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount=web3.eth.accounts[0]
print(web3.isConnected())
abi=json.loads('[{"inputs":[],"name":"Manager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"uuid","type":"string"},{"internalType":"uint256","name":"p_no","type":"uint256"}],"name":"Vote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"uuid","type":"string"},{"internalType":"uint256","name":"p_no","type":"uint256"}],"name":"Votea","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"uuid","type":"string"},{"internalType":"uint256","name":"p_no","type":"uint256"}],"name":"Voteu","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"Winner","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Winnera","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Winnerdetails","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Winneru","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"c_name","type":"string"},{"internalType":"uint256","name":"age","type":"uint256"},{"internalType":"uint256","name":"p_no","type":"uint256"}],"name":"addCandidate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"v_name","type":"string"},{"internalType":"uint256","name":"age","type":"uint256"},{"internalType":"string","name":"pannumber","type":"string"},{"internalType":"string","name":"uuid","type":"string"}],"name":"addVoter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"arr","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"arra","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"arru","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"candidates","outputs":[{"internalType":"string","name":"c_name","type":"string"},{"internalType":"uint256","name":"age","type":"uint256"},{"internalType":"uint256","name":"p_no","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"voters","outputs":[{"internalType":"string","name":"v_name","type":"string"},{"internalType":"uint256","name":"age","type":"uint256"},{"internalType":"string","name":"pannumber","type":"string"},{"internalType":"string","name":"uuid","type":"string"},{"internalType":"uint256","name":"ticket","type":"uint256"},{"internalType":"bool","name":"voted","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"x","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"xa","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"xu","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

bytecode="608060405234801561001057600080fd5b5061170f806100206000396000f3fe608060405234801561001057600080fd5b50600436106101215760003560e01c806371e5ee5f116100ad578063b2b98ed211610071578063b2b98ed2146102dc578063c5539cc2146102fb578063e2a781251461032d578063e953df3114610349578063ef84b88e1461036857610121565b806371e5ee5f1461024e57806376fc96cb1461027e57806378357e531461029a5780637ce74022146102a45780639c63d42e146102c057610121565b8063102f89c9116100f4578063102f89c9146101af5780631970e446146101d5578063481c6a75146101f157806353fa2e641461020f57806357ac46f51461024457610121565b806305d3a7d314610126578063092e0acd146101565780630c55699c146101865780630f6da28714610190575b600080fd5b610140600480360381019061013b919061115d565b610372565b60405161014d9190611307565b60405180910390f35b610170600480360381019061016b919061115d565b61038d565b60405161017d9190611307565b60405180910390f35b61018e6103a8565b005b6101986103e5565b6040516101a6929190611322565b60405180910390f35b6101b761045f565b6040516101cc9998979695949392919061134b565b60405180910390f35b6101ef60048036038101906101ea91906110ee565b610558565b005b6101f96105ca565b6040516102069190611238565b60405180910390f35b61022960048036038101906102249190610f8e565b6105ee565b60405161023b96959493929190611253565b60405180910390f35b61024c6107e5565b005b6102686004803603810190610263919061115d565b610822565b6040516102759190611307565b60405180910390f35b61029860048036038101906102939190611033565b61083d565b005b6102a261092e565b005b6102be60048036038101906102b99190610fd7565b610970565b005b6102da60048036038101906102d59190610fd7565b610a6f565b005b6102e4610b6e565b6040516102f2929190611322565b60405180910390f35b61031560048036038101906103109190610f8e565b610be8565b604051610324939291906112c9565b60405180910390f35b61034760048036038101906103429190610fd7565b610cb0565b005b610351610daf565b60405161035f929190611322565b60405180910390f35b610370610e29565b005b6035816019811061038257600080fd5b016000915090505481565b601c816019811061039d57600080fd5b016000915090505481565b60005b60198110156103e2576000600382601981106103ca576103c961163f565b5b018190555080806103da90611598565b9150506103ab565b50565b6000806000805b601981101561043e57603582601981106104095761040861163f565b5b01546035826019811061041f5761041e61163f565b5b0154111561042b578091505b808061043690611598565b9150506103ec565b81603583601981106104535761045261163f565b5b01549350935050509091565b600080600080600080600080600060036001601981106104825761048161163f565b5b015460036002601981106104995761049861163f565b5b0154600380601981106104af576104ae61163f565b5b0154601c6001601981106104c6576104c561163f565b5b0154601c6002601981106104dd576104dc61163f565b5b0154601c6003601981106104f4576104f361163f565b5b0154603560016019811061050b5761050a61163f565b5b015460356002601981106105225761052161163f565b5b015460356003601981106105395761053861163f565b5b0154985098509850985098509850985098509850909192939495969798565b6040518060600160405280848152602001838152602001828152506001846040516105839190611221565b908152602001604051809103902060008201518160000190805190602001906105ad929190610e66565b506020820151816001015560408201518160020155905050505050565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60028180516020810182018051848252602083016020850120818352809550505050505060009150905080600001805461062790611535565b80601f016020809104026020016040519081016040528092919081815260200182805461065390611535565b80156106a05780601f10610675576101008083540402835291602001916106a0565b820191906000526020600020905b81548152906001019060200180831161068357829003601f168201915b5050505050908060010154908060020180546106bb90611535565b80601f01602080910402602001604051908101604052809291908181526020018280546106e790611535565b80156107345780601f1061070957610100808354040283529160200191610734565b820191906000526020600020905b81548152906001019060200180831161071757829003601f168201915b50505050509080600301805461074990611535565b80601f016020809104026020016040519081016040528092919081815260200182805461077590611535565b80156107c25780601f10610797576101008083540402835291602001916107c2565b820191906000526020600020905b8154815290600101906020018083116107a557829003601f168201915b5050505050908060040154908060050160009054906101000a900460ff16905086565b60005b601981101561081f576000603582601981106108075761080661163f565b5b0181905550808061081790611598565b9150506107e8565b50565b6003816019811061083257600080fd5b016000915090505481565b601283101561084b57600080fd5b6040518060c00160405280858152602001848152602001838152602001828152602001600181526020016000151581525060028260405161088c9190611221565b908152602001604051809103902060008201518160000190805190602001906108b6929190610e66565b506020820151816001015560408201518160020190805190602001906108dd929190610e66565b5060608201518160030190805190602001906108fa929190610e66565b506080820151816004015560a08201518160050160006101000a81548160ff02191690831515021790555090505050505050565b336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550565b600015156002836040516109849190611221565b908152602001604051809103902060050160009054906101000a900460ff161515146109af57600080fd5b60016002836040516109c19190611221565b908152602001604051809103902060040154146109dd57600080fd5b6001603582601981106109f3576109f261163f565b5b016000828254610a039190611455565b925050819055506001600283604051610a1c9190611221565b908152602001604051809103902060050160006101000a81548160ff0219169083151502179055506000600283604051610a569190611221565b9081526020016040518091039020600401819055505050565b60001515600283604051610a839190611221565b908152602001604051809103902060050160009054906101000a900460ff16151514610aae57600080fd5b6001600283604051610ac09190611221565b90815260200160405180910390206004015414610adc57600080fd5b600160038260198110610af257610af161163f565b5b016000828254610b029190611455565b925050819055506001600283604051610b1b9190611221565b908152602001604051809103902060050160006101000a81548160ff0219169083151502179055506000600283604051610b559190611221565b9081526020016040518091039020600401819055505050565b6000806000805b6019811015610bc75760038260198110610b9257610b9161163f565b5b015460038260198110610ba857610ba761163f565b5b01541115610bb4578091505b8080610bbf90611598565b915050610b75565b8160038360198110610bdc57610bdb61163f565b5b01549350935050509091565b600181805160208101820180518482526020830160208501208183528095505050505050600091509050806000018054610c2190611535565b80601f0160208091040260200160405190810160405280929190818152602001828054610c4d90611535565b8015610c9a5780601f10610c6f57610100808354040283529160200191610c9a565b820191906000526020600020905b815481529060010190602001808311610c7d57829003601f168201915b5050505050908060010154908060020154905083565b60001515600283604051610cc49190611221565b908152602001604051809103902060050160009054906101000a900460ff16151514610cef57600080fd5b6001600283604051610d019190611221565b90815260200160405180910390206004015414610d1d57600080fd5b6001601c8260198110610d3357610d3261163f565b5b016000828254610d439190611455565b925050819055506001600283604051610d5c9190611221565b908152602001604051809103902060050160006101000a81548160ff0219169083151502179055506000600283604051610d969190611221565b9081526020016040518091039020600401819055505050565b6000806000805b6019811015610e0857601c8260198110610dd357610dd261163f565b5b0154601c8260198110610de957610de861163f565b5b01541115610df5578091505b8080610e0090611598565b915050610db6565b81601c8360198110610e1d57610e1c61163f565b5b01549350935050509091565b60005b6019811015610e63576000601c8260198110610e4b57610e4a61163f565b5b01819055508080610e5b90611598565b915050610e2c565b50565b828054610e7290611535565b90600052602060002090601f016020900481019282610e945760008555610edb565b82601f10610ead57805160ff1916838001178555610edb565b82800160010185558215610edb579182015b82811115610eda578251825591602001919060010190610ebf565b5b509050610ee89190610eec565b5090565b5b80821115610f05576000816000905550600101610eed565b5090565b6000610f1c610f17846113fd565b6113d8565b905082815260208101848484011115610f3857610f376116a2565b5b610f438482856114f3565b509392505050565b600082601f830112610f6057610f5f61169d565b5b8135610f70848260208601610f09565b91505092915050565b600081359050610f88816116c2565b92915050565b600060208284031215610fa457610fa36116ac565b5b600082013567ffffffffffffffff811115610fc257610fc16116a7565b5b610fce84828501610f4b565b91505092915050565b60008060408385031215610fee57610fed6116ac565b5b600083013567ffffffffffffffff81111561100c5761100b6116a7565b5b61101885828601610f4b565b925050602061102985828601610f79565b9150509250929050565b6000806000806080858703121561104d5761104c6116ac565b5b600085013567ffffffffffffffff81111561106b5761106a6116a7565b5b61107787828801610f4b565b945050602061108887828801610f79565b935050604085013567ffffffffffffffff8111156110a9576110a86116a7565b5b6110b587828801610f4b565b925050606085013567ffffffffffffffff8111156110d6576110d56116a7565b5b6110e287828801610f4b565b91505092959194509250565b600080600060608486031215611107576111066116ac565b5b600084013567ffffffffffffffff811115611125576111246116a7565b5b61113186828701610f4b565b935050602061114286828701610f79565b925050604061115386828701610f79565b9150509250925092565b600060208284031215611173576111726116ac565b5b600061118184828501610f79565b91505092915050565b611193816114ab565b82525050565b6111a2816114bd565b82525050565b60006111b38261142e565b6111bd8185611439565b93506111cd818560208601611502565b6111d6816116b1565b840191505092915050565b60006111ec8261142e565b6111f6818561144a565b9350611206818560208601611502565b80840191505092915050565b61121b816114e9565b82525050565b600061122d82846111e1565b915081905092915050565b600060208201905061124d600083018461118a565b92915050565b600060c082019050818103600083015261126d81896111a8565b905061127c6020830188611212565b818103604083015261128e81876111a8565b905081810360608301526112a281866111a8565b90506112b16080830185611212565b6112be60a0830184611199565b979650505050505050565b600060608201905081810360008301526112e381866111a8565b90506112f26020830185611212565b6112ff6040830184611212565b949350505050565b600060208201905061131c6000830184611212565b92915050565b60006040820190506113376000830185611212565b6113446020830184611212565b9392505050565b600061012082019050611361600083018c611212565b61136e602083018b611212565b61137b604083018a611212565b6113886060830189611212565b6113956080830188611212565b6113a260a0830187611212565b6113af60c0830186611212565b6113bc60e0830185611212565b6113ca610100830184611212565b9a9950505050505050505050565b60006113e26113f3565b90506113ee8282611567565b919050565b6000604051905090565b600067ffffffffffffffff8211156114185761141761166e565b5b611421826116b1565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b600081905092915050565b6000611460826114e9565b915061146b836114e9565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff038211156114a05761149f6115e1565b5b828201905092915050565b60006114b6826114c9565b9050919050565b60008115159050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b83811015611520578082015181840152602081019050611505565b8381111561152f576000848401525b50505050565b6000600282049050600182168061154d57607f821691505b6020821081141561156157611560611610565b5b50919050565b611570826116b1565b810181811067ffffffffffffffff8211171561158f5761158e61166e565b5b80604052505050565b60006115a3826114e9565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8214156115d6576115d56115e1565b5b600182019050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b6116cb816114e9565b81146116d657600080fd5b5056fea2646970667358221220fc19ffa4363482d66c3c74bc499b9edc28d62f9a446bfd451d5a798758ca8b5664736f6c63430008070033"

Manager = web3.eth.contract(abi=abi,bytecode=bytecode)
# address = web3.toChecksumAddress("0xA15893D5Fd4F8c9eE31BAe37738b98e3D33918E0")

# contract = web3.eth.contract(address=address, abi=abi)
# x = contract.functions.greet().call()
tx_hash=Manager.constructor().transact()
print(tx_hash)

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

contract=web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# print(contract.functions.greet().call())

# tx_hash=contract.functions.setGreeting("Heeeeeelllllllloooooooooo!!").transact()
# tx_hash=contract.functions.addCandidate("Vansh",33,1).transact()
# tx_hash=contract.functions.addCandidate("ansh",43,2).transact()
# tx_hash=contract.functions.addVoter("Vinayak",33).transact()
# tx_hash=contract.functions.addVoter("sak",53).transact()

# contract.functions.Vote("Vinayak",2).transact()
# contract.functions.Vote("sak",2).transact()
# print(contract.functions.Winner().call())

def vote(name,age,pan_no,uuid):
    tx_hash = contract.functions.addVoter(name,age,pan_no,uuid).transact()
    # tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    # print(contract.functions.List(uuid).call())
    print(uuid)
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# print(contract.functions.greet().call())
def reset():
    contract.functions.x().transact()

def reseta():
    contract.functions.xa().transact()

def resetu():
    contract.functions.xu().transact()

def Voting1u(uuid):
    tx_hash=contract.functions.Voteu(uuid,1).transact()
    print(tx_hash)
    print("111111111")
    print("111111111")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_******")
    print("_____*****")
    print("_____")
    print("_____")
    print("_____")

def Voting2u(uuid):
    tx_hash=contract.functions.Voteu(uuid,2).transact()
    print("22222222")
    print("22222222")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")

def Voting3u(uuid):
    tx_hash=contract.functions.Voteu(uuid,3).transact()
    print("3333333")
    print("3333333")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")


def Voting1a(uuid):
    tx_hash=contract.functions.Votea(uuid,1).transact()
    print(tx_hash)
    print("111111111")
    print("111111111")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_******")
    print("_____*****")
    print("_____")
    print("_____")
    print("_____")

def Voting2a(uuid):
    tx_hash=contract.functions.Votea(uuid,2).transact()
    print("22222222")
    print("22222222")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")

def Voting3a(uuid):
    tx_hash=contract.functions.Votea(uuid,3).transact()
    print("3333333")
    print("3333333")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")

def Voting1(uuid):
    tx_hash=contract.functions.Vote(uuid,1).transact()
    print(tx_hash)
    print("111111111")
    print("111111111")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_******")
    print("_____*****")
    print("_____")
    print("_____")
    print("_____")

def Voting2(uuid):
    tx_hash=contract.functions.Vote(uuid,2).transact()
    print("22222222")
    print("22222222")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")

def Voting3(uuid):
    tx_hash=contract.functions.Vote(uuid,3).transact()
    print("3333333")
    print("3333333")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")
    print("_____")

def abcd():
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_______")
    print("_____")
    print("_____")
    print("_____")
    # print(contract.functions.Winner().call())
    print("_____")
    print("_____")
    print("_____")

def winner():
    print("The Winner of Palghar is as follows")
    return contract.functions.Winner().call()

def winnera():
    print("The Winner of Amroha is as follows")
    return contract.functions.Winnera().call()

def winneru():
    print("The Winner of Udma is as follows")
    return contract.functions.Winneru().call()

def winnerdetails():
    print("The full voting details is as follows\n\n\n")
    return contract.functions.Winnerdetails().call()
    reset()
    reseta()
    resetu()



# resetu()
# reset()
# reseta()