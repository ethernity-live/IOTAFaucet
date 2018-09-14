This is a Faucet for IOTA

Built for AcuWiki.com

To connect to the IOTA network we use iotaproxy (https://github.com/TimSamshuijzen/iotaproxy/). Very easy-to-use. This proxy makes all PoW locally and connects to a public node.

The Faucet is designed to work with the WordPress wp_users table and can be easily tweaked.

Steps:

- Get total balance in IOTAS
- Calculate amount to pay according to config
- Get a list of members with their reputation points and IOTA address (can be null)
- Makes payment. When making the payment, the system will calculate a "IOTAs per reputation point" and send to each user having a valid IOTA address.



