# tokens

A list of NEP5 tokens that held an ICO along their corresponding ICO start/end dates.

This list is used by [neon-wallet](https://github.com/CityOfZion/neon-wallet) to determine which
tokens can be purchased via the token sale screen.

## Adding Tokens

If your NEP5 token is having a public token sale (ICO), add it to the `tokens.json` file for it to
appear in Neon Wallet for the duration of the sale.  If your token is not having a sale, but is
instead being airdropped, then there is no need to add it to this repository.

All tokens listed in the `tokens.json` file must take the following structure:

```js
{
  // NEP5 token symbol
  "symbol": "XXX",
  // NEP5 token script hash
  "scriptHash": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  // token sale start date/time (UTC)
  "start": "YYYY-MM-DD HH:MM:SS",
  // token sale end date/time (UTC)
  "end": "YYYY-MM-DD HH:MM:SS"
}
```

When adding your token, please ensure that it appears alphabetically by token symbol for ease of
maintenance.
