# Upsonic Auth

The cloud authentication save system for your python applications ! Control everything from one place and distribute all clients without effort.

[Website](https://upsonic.co/upsonic-auth) | [Discord](https://discord.gg/) | [Twitter](https://twitter.com/upsonicco)




## Installation
You can install Upsonic by pip3:

```console
pip3 install upsonic_auth
```




# Implementing

## 1) Encrypted and Free Version
We suggest to use in your individual projects because this way not provide any control process so everyone can add credientials.

*Creating Your Free Cloud Key
```console
Upsonic cloud_key
```

```python
from upsonic_auth import Upsonic_Auth
auth = Upsonic_Auth("YOUR_ENCRYPTION_KEY", "YOUR_CLOUD_KEY")

auth.add_user("Name", "Pass")
#auth.delete_user("Name")

if auth.check("name", "Pass"): # In another.py, Diffferent Machine, Different Environment
    print("Verified")
```


## 2) Encrypted and Pro Version
We suggest to use in your individual projects because this way not provide any control process so everyone can add credientials.

*For this you should have [Upsonic Cloud Pro](https://docs.upsonic.co/upsonic_cloud.html#cloud-pro--)

```python
from upsonic_auth import Upsonic_Auth_Pro
auth = Upsonic_Auth_Pro("YOUR_ENCRYPTION_KEY", "YOUR_CLOUD_PRO_KEY", "YOUR_ACCESS_KEY")

auth.add_user("Name", "Pass")
#auth.delete_user("Name")


if auth.check("name", "Pass"): # In another.py, Diffferent Machine, Different Environment
    print("Verified")
```

## 3) Encrypted and Secure Version
You can free for all purposes.


*For this you should have [Upsonic Cloud Dedicated](https://docs.upsonic.co/upsonic_cloud.html#cloud-dedicated)


```python
from upsonic_auth import Upsonic_Auth_Dedicated
auth = Upsonic_Auth_Dedicated("YOUR_ENCRYPTION_KEY", "YOUR_DATABASE_NAME", "YOUR_ADMIN_PASSWORD", "YOUR_DEDICATED_KEY")

auth.add_user("Name", "Pass")
#auth.delete_user("Name")

auth = Upsonic_Auth_Dedicated("YOUR_DATABASE_NAME", "YOUR_USER_PASSWORD", "YOUR_DEDICATED_KEY")

if auth.check("name", "Pass"): # In another.py, Diffferent Machine, Different Environment and CUSTOMER
    print("Verified")
```





## Contributing
Contributions to Upsonic Auth are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
Upsonic Auth is released under the MIT License.

<h2 align="center">
    Contributors
</h2>
<p align="center">
    Thank you for your contribution!
</p>
<p align="center">
    <a href="https://github.com/Upsonic/Upsonic-Auth/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Upsonic/Upsonic-Auth" />
    </a>
</p>
