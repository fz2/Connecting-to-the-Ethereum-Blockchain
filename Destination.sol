// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "./BridgeToken.sol";

contract Destination is AccessControl {
    bytes32 public constant WARDEN_ROLE = keccak256("BRIDGE_WARDEN_ROLE");
    bytes32 public constant CREATOR_ROLE = keccak256("CREATOR_ROLE");
	mapping( address => address) public underlying_tokens;
	mapping( address => address) public wrapped_tokens;
	address[] public tokens;

	event Creation( address indexed underlying_token, address indexed wrapped_token );
	event Wrap( address indexed underlying_token, address indexed wrapped_token, address indexed to, uint256 amount );
	event Unwrap( address indexed underlying_token, address indexed wrapped_token, address frm, address indexed to, uint256 amount );

    constructor( address admin ) {
        _grantRole(DEFAULT_ADMIN_ROLE, admin);
        _grantRole(CREATOR_ROLE, admin);
        _grantRole(WARDEN_ROLE, admin);
    }

	function wrap(address _underlying_token, address _recipient, uint256 _amount ) public onlyRole(WARDEN_ROLE) {
		//This function should lookup the BridgeToken that corresponds to the underlying asset, and mint the correct amount of BridgeTokens to the recipient.
    // This function must check that underlying asset has been “registered,” i.e., that the owner of the destination contract has called createToken on the underlying asset.

		//_mint(_underlying_token, _amount)
	}

	function unwrap(address _wrapped_token, address _recipient, uint256 _amount ) public {
		//YOUR CODE HERE, Anyone should be able to unwrap BridgeTokens, but only tokens they own.
		//_burnfrom(_wrapped_token, _amount)
	}
	function createToken(address _underlying_token, string memory name, string memory symbol ) public onlyRole(CREATOR_ROLE) returns(address) {
		// When the createToken function is called, it will deploy a new BridgeToken contract, and return the address of the newly created contract.
    require(msg.sender == CREATOR_ROLE);
    BridgeToken newToken = BridgeToken(_underlying_token,name,symbol, CREATOR_ROLE);
    emit Creation(_underlying_token, newToken.address);
    return newToken.address;

	}
}

