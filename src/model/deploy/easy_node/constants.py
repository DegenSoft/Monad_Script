# Первый вариант байткода контракта
DEPLOY_CONTRACT_BYTECODE_1 = "0x608060405260405162001580380380620015808339818101604052810190620000299190620004fc565b600034116200006f576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401620000669062000623565b60405180910390fd5b60003411156200012e5760008173ffffffffffffffffffffffffffffffffffffffff1634604051620000a1906200067a565b60006040518083038185875af1925050503d8060008114620000e0576040519150601f19603f3d011682016040523d82523d6000602084013e620000e5565b606091505b50509050806200012c576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016200012390620006e1565b60405180910390fd5b505b846000908051906020019062000146929190620001d1565b5083600190805190602001906200015f929190620001d1565b5082600260006101000a81548160ff021916908360ff1602179055508160038190555081600460003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550505050505062000768565b828054620001df9062000732565b90600052602060002090601f0160209004810192826200020357600085556200024f565b82601f106200021e57805160ff19168380011785556200024f565b828001600101855582156200024f579182015b828111156200024e57825182559160200191906001019062000231565b5b5090506200025e919062000262565b5090565b5b808211156200027d57600081600090555060010162000263565b5090565b6000604051905090565b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b620002ea826200029f565b810181811067ffffffffffffffff821117156200030c576200030b620002b0565b5b80604052505050565b60006200032162000281565b90506200032f8282620002df565b919050565b600067ffffffffffffffff821115620003525762000351620002b0565b5b6200035d826200029f565b9050602081019050919050565b60005b838110156200038a5780820151818401526020810190506200036d565b838111156200039a576000848401525b50505050565b6000620003b7620003b18462000334565b62000315565b905082815260208101848484011115620003d657620003d56200029a565b5b620003e38482856200036a565b509392505050565b600082601f83011262000403576200040262000295565b5b815162000415848260208601620003a0565b91505092915050565b600060ff82169050919050565b62000436816200041e565b81146200044257600080fd5b50565b60008151905062000456816200042b565b92915050565b6000819050919050565b62000471816200045c565b81146200047d57600080fd5b50565b600081519050620004918162000466565b92915050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000620004c48262000497565b9050919050565b620004d681620004b7565b8114620004e257600080fd5b50565b600081519050620004f681620004cb565b92915050565b600080600080600060a086880312156200051b576200051a6200028b565b5b600086015167ffffffffffffffff8111156200053c576200053b62000290565b5b6200054a88828901620003eb565b955050602086015167ffffffffffffffff8111156200056e576200056d62000290565b5b6200057c88828901620003eb565b94505060406200058f8882890162000445565b9350506060620005a28882890162000480565b9250506080620005b588828901620004e5565b9150509295509295909350565b600082825260208201905092915050565b7f4465706c6f796d656e7420726571756972657320612066656500000000000000600082015250565b60006200060b601983620005c2565b91506200061882620005d3565b602082019050919050565b600060208201905081810360008301526200063e81620005fc565b9050919050565b600081905092915050565b50565b60006200066260008362000645565b91506200066f8262000650565b600082019050919050565b6000620006878262000653565b9150819050919050565b7f466565207472616e73666572206661696c656400000000000000000000000000600082015250565b6000620006c9601383620005c2565b9150620006d68262000691565b602082019050919050565b60006020820190508181036000830152620006fc81620006ba565b9050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b600060028204905060018216806200074b57607f821691505b6020821081141562000762576200076162000703565b5b50919050565b610e0880620007786000396000f3fe608060405234801561001057600080fd5b50600436106100935760003560e01c8063313ce56711610066578063313ce5671461013457806370a082311461015257806395d89b4114610182578063a9059cbb146101a0578063dd62ed3e146101d057610093565b806306fdde0314610098578063095ea7b3146100b657806318160ddd146100e657806323b872dd14610104575b600080fd5b6100a0610200565b6040516100ad919061098e565b60405180910390f35b6100d060048036038101906100cb9190610a49565b61028e565b6040516100dd9190610aa4565b60405180910390f35b6100ee610380565b6040516100fb9190610ace565b60405180910390f35b61011e60048036038101906101199190610ae9565b610386565b60405161012b9190610aa4565b60405180910390f35b61013c610678565b6040516101499190610b58565b60405180910390f35b61016c60048036038101906101679190610b73565b61068b565b6040516101799190610ace565b60405180910390f35b61018a6106a3565b604051610197919061098e565b60405180910390f35b6101ba60048036038101906101b59190610a49565b610731565b6040516101c79190610aa4565b60405180910390f35b6101ea60048036038101906101e59190610ba0565b6108d0565b6040516101f79190610ace565b60405180910390f35b6000805461020d90610c0f565b80601f016020809104026020016040519081016040528092919081815260200182805461023990610c0f565b80156102865780601f1061025b57610100808354040283529160200191610286565b820191906000526020600020905b81548152906001019060200180831161026957829003601f168201915b505050505081565b600081600560003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b9258460405161036e9190610ace565b60405180910390a36001905092915050565b60035481565b600081600460008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054101561040a576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161040190610c8d565b60405180910390fd5b81600560008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410156104c9576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016104c090610cf9565b60405180910390fd5b81600460008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546105189190610d48565b9250508190555081600460008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461056e9190610d7c565b9250508190555081600560008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546106019190610d48565b925050819055508273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040516106659190610ace565b60405180910390a3600190509392505050565b600260009054906101000a900460ff1681565b60046020528060005260406000206000915090505481565b600180546106b090610c0f565b80601f01602080910402602001604051908101604052809291908181526020018280546106dc90610c0f565b80156107295780601f106106fe57610100808354040283529160200191610729565b820191906000526020600020905b81548152906001019060200180831161070c57829003601f168201915b505050505081565b600081600460003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410156107b5576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107ac90610c8d565b60405180910390fd5b81600460003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546108049190610d48565b9250508190555081600460008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461085a9190610d7c565b925050819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040516108be9190610ace565b60405180910390a36001905092915050565b6005602052816000526040600020602052806000526040600020600091509150505481565b600081519050919050565b600082825260208201905092915050565b60005b8381101561092f578082015181840152602081019050610914565b8381111561093e576000848401525b50505050565b6000601f19601f8301169050919050565b6000610960826108f5565b61096a8185610900565b935061097a818560208601610911565b61098381610944565b840191505092915050565b600060208201905081810360008301526109a88184610955565b905092915050565b600080fd5b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006109e0826109b5565b9050919050565b6109f0816109d5565b81146109fb57600080fd5b50565b600081359050610a0d816109e7565b92915050565b6000819050919050565b610a2681610a13565b8114610a3157600080fd5b50565b600081359050610a4381610a1d565b92915050565b60008060408385031215610a6057610a5f6109b0565b5b6000610a6e858286016109fe565b9250506020610a7f85828601610a34565b9150509250929050565b60008115159050919050565b610a9e81610a89565b82525050565b6000602082019050610ab96000830184610a95565b92915050565b610ac881610a13565b82525050565b6000602082019050610ae36000830184610abf565b92915050565b600080600060608486031215610b0257610b016109b0565b5b6000610b10868287016109fe565b9350506020610b21868287016109fe565b9250506040610b3286828701610a34565b9150509250925092565b600060ff82169050919050565b610b5281610b3c565b82525050565b6000602082019050610b6d6000830184610b49565b92915050565b600060208284031215610b8957610b886109b0565b5b6000610b97848285016109fe565b91505092915050565b60008060408385031215610bb757610bb66109b0565b5b6000610bc5858286016109fe565b9250506020610bd6858286016109fe565b9150509250929050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b60006002820490506001821680610c2757607f821691505b60208210811415610c3b57610c3a610be0565b5b50919050565b7f496e73756666696369656e742062616c616e6365000000000000000000000000600082015250565b6000610c77601483610900565b9150610c8282610c41565b602082019050919050565b60006020820190508181036000830152610ca681610c6a565b9050919050565b7f496e73756666696369656e7420616c6c6f77616e636500000000000000000000600082015250565b6000610ce3601683610900565b9150610cee82610cad565b602082019050919050565b60006020820190508181036000830152610d1281610cd6565b9050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b6000610d5382610a13565b9150610d5e83610a13565b925082821015610d7157610d70610d19565b5b828203905092915050565b6000610d8782610a13565b9150610d9283610a13565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03821115610dc757610dc6610d19565b5b82820190509291505056fea2646970667358221220495ea7d65c750e22a8696ca755a4becc666a16fd223656da810a79c61f2005e964736f6c6343000809003300000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000000000000000000000000000000000000000001200000000000000000000000000000000000000000000d3c21bcecceda1000000000000000000000000000000fda77b68d08988e91932a3a4ff4d49d4771536f800000000000000000000000000000000000000000000000000000000000000084d7920546f6b656e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000034d544b0000000000000000000000000000000000000000000000000000000000"  # Здесь нужно вставить первый байткод

# Второй вариант байткода контракта
DEPLOY_CONTRACT_BYTECODE_2 = "0x608060405260405161052438038061052483398181016040528101906100259190610188565b60003411610068576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161005f90610212565b60405180910390fd5b600034111561011f5760008173ffffffffffffffffffffffffffffffffffffffff163460405161009790610263565b60006040518083038185875af1925050503d80600081146100d4576040519150601f19603f3d011682016040523d82523d6000602084013e6100d9565b606091505b505090508061011d576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610114906102c4565b60405180910390fd5b505b506102e4565b600080fd5b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006101558261012a565b9050919050565b6101658161014a565b811461017057600080fd5b50565b6000815190506101828161015c565b92915050565b60006020828403121561019e5761019d610125565b5b60006101ac84828501610173565b91505092915050565b600082825260208201905092915050565b7f4465706c6f796d656e7420726571756972657320612066656500000000000000600082015250565b60006101fc6019836101b5565b9150610207826101c6565b602082019050919050565b6000602082019050818103600083015261022b816101ef565b9050919050565b600081905092915050565b50565b600061024d600083610232565b91506102588261023d565b600082019050919050565b600061026e82610240565b9150819050919050565b7f466565207472616e73666572206661696c656400000000000000000000000000600082015250565b60006102ae6013836101b5565b91506102b982610278565b602082019050919050565b600060208201905081810360008301526102dd816102a1565b9050919050565b610231806102f36000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c80632baeceb714610046578063a87d942c14610050578063d09de08a1461006e575b600080fd5b61004e610078565b005b6100586100ca565b604051610065919061013e565b60405180910390f35b6100766100d3565b005b60008081548092919061008a90610188565b91905055507f1a00a27c962d5410357331e1a8cffff62058bd0161ad624818df31152f1eeb456000546040516100c0919061013e565b60405180910390a1565b60008054905090565b6000808154809291906100e5906101b2565b91905055507f3cf8b50771c17d723f2cb711ca7dadde485b222e13c84ba0730a14093fad6d5c60005460405161011b919061013e565b60405180910390a1565b6000819050919050565b61013881610125565b82525050565b6000602082019050610153600083018461012f565b92915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b600061019382610125565b915060008214156101a7576101a6610159565b5b600182039050919050565b60006101bd82610125565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8214156101f0576101ef610159565b5b60018201905091905056fea2646970667358221220526250c31d8148ffcfa6d06ab24c6dfbf02441f204c5578890519ec2fdd071c564736f6c63430008090033000000000000000000000000fda77b68d08988e91932a3a4ff4d49d4771536f8"  # Здесь нужно вставить второй байткод