// contracts/VinauToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract VianuToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("VianuTok", "VIT") {
        _mint(msg.sender, initialSupply);
    }
}
