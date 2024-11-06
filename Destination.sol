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
    // This function must check that underlying asset has been “registered,” i.e., that the owner of the destination contract has called createToken on the underlying asset.
    burnfrom(_underlying_token, _amount);
		mint(_recipient, _amount);
    emit Wrap(_underlying_token, address(this), _recipient, _amount);
	}

	function unwrap(address _wrapped_token, address _recipient, uint256 _amount ) public {
		//YOUR CODE HERE, Anyone should be able to unwrap BridgeTokens, but only tokens they own.
		burnfrom(_wrapped_token, _amount);
	}

	function createToken(address _underlying_token, string memory name, string memory symbol ) public onlyRole(CREATOR_ROLE) returns(address) {
		// When the createToken function is called, it will deploy a new BridgeToken contract, and return the address of the newly created contract.
    BridgeToken newToken = new BridgeToken(_underlying_token, name,symbol, address(this));
    underlying_tokens[_underlying_token] = _underlying_token;
    wrapped_tokens[address(this)] = address(this);
    tokens.push(address(newToken));
    emit Creation(_underlying_token, address(newToken));
    return address(newToken);
	}
}


