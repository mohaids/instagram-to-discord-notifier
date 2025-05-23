# GPG - How it works

### Overview
Definition: GPG is short for GNU Privacy Guard - a method to securely verify that the data (ex. software) you're installing hasn't been tampered with.

#### Overview of process:
1. Get their (the party who's software you want to download) public GPG key
2. Verify the key is authentic (confirming GPG's hash is the same as the party's hash)
3. Import key into your GPG keyring
4. Download the actual data you want to download
5. Download the data's signature
6. Now use their public GPG key and compare it with the data's signature to detemine if the data hasn't been tampered with.
7. Once GPG confirms validity and non-tampering, you can open the data.

#### Walkthrough with Mullvad VPN

**Step 1:** Getting Mullvad's public GPG key
```shell
wget https://mullvad.net/media/mullvad-code-signing.asc
```

**Step 2:** Add the key to your keyring
```shell
gpg --import mullvad-code-signing.asc
```

```output
gpg: key D5A1D4F266DE8DDF: public key "Mullvad (code signing) <admin@mullvad.net>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


**Step 3:** Verifying the key is authentic (meaning the fingerprint of the GPG equals the fingerprint that Mullvad provides on their website)

```shell
gpg --fingerprint admin@mullvad.net
```

```text
where did "admin@mullvad.net" come from - this information is contained in the gpg key

for general case: when importing key into keyring, look at the output (step 2) - this is where the email will be
```

Compare the output of the above command to the fingerprint reported by Mullvad on their [site](https://mullvad.net/en/help/verifying-signatures)

```output
truncated output: 
pub   rsa4096 2016-10-27 [SC]
      A119 8702 FC3E 0A09 A9AE  5B75 D5A1 D4F2 66DE 8DDF
```

**Step 4:** Download the actual Mullvad VPN software
```shell
wget --trust-server-names https://mullvad.net/download/app/deb/latest
```

**Step 5:** Download the software's signature
```shell
wget --trust-server-names https://mullvad.net/download/app/deb/latest/signature
```

**Step 6:** Verify the software's signature
```shell
gpg --verify MullvadVPN-*.deb.asc
```

**Questions:** why aren't we checking the software's file as well? like why just the signature? 

If the output returns the following, it's confirmed to be authentic:
```output
gpg: Good signature from "Mullvad (code signing) <admin@mullvad.net>" [full]
```

**Step 7:** Open the package 😊🚀
```shell
sudo dpkg -i MullvadVPN-*.deb
```