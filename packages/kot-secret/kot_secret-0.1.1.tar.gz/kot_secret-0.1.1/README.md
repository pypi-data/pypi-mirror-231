# KOT Secret

The cloud secret save system for your python applications ! Control everything from one place and distribute all clients without effort.

[Website](https://kotdatabase.dev/) | [Discord](https://discord.gg/QtnKf532Er) | [Twitter](https://twitter.com/kot_database)




## Installation
You can install KOT by pip3:

```console
pip3 install kot_secret
```




# Implementing

## 1) Encrypted and Free Version
We suggest to use in your individual projects because this way not provide any control process so everyone can add credientials.

*Creating Your Free Cloud Key
```console
KOT cloud_key
```

```python
from kot_secret import KOT_Secret
secrets = KOT_Secret("YOUR_ENCRYPTION_KEY", "YOUR_CLOUD_KEY")

secrets.add_secret("SECRET_NAME", "SECRET")
#secrets.delete_secret("SECRET_NAME")

secrets.get_secret("SECRET_NAME") # In another.py, Diffferent Machine, Different Environment
```


## 2) Encrypted and Pro Version
We suggest to use in your individual projects because this way not provide any control process so everyone can add credientials.

*For this you should have [KOT Cloud Pro](https://docs.kotdatabase.dev/kot_cloud.html#cloud-pro--)

```python
from kot_secret import KOT_Secret_Pro
secrets = KOT_Secret_Pro("YOUR_ENCRYPTION_KEY", "YOUR_CLOUD_PRO_KEY", "YOUR_ACCESS_KEY")

secrets.add_secret("SECRET_NAME", "SECRET")
#secrets.delete_secret("SECRET_NAME")

secrets.get_secret("SECRET_NAME")# In another.py, Diffferent Machine, Different Environment
```

## 3) Encrypted and Secure Version
You can free for all purposes.


*For this you should have [KOT Cloud Dedicated](https://docs.kotdatabase.dev/kot_cloud.html#cloud-dedicated)


```python
from kot_secret import KOT_Secret_Dedicated
secrets = KOT_Secret_Dedicated("YOUR_ENCRYPTION_KEY", "YOUR_DATABASE_NAME", "YOUR_ADMIN_PASSWORD", "YOUR_DEDICATED_KEY")

secrets.add_secret("SECRET_NAME", "SECRET")
#secrets.delete_secret("SECRET_NAME")

secrets = KOT_Secret_Dedicated("YOUR_ENCRYPTION_KEY", "YOUR_DATABASE_NAME", "YOUR_USER_PASSWORD", "YOUR_DEDICATED_KEY")

secrets.get_secret("SECRET_NAME") # In another.py, Diffferent Machine, Different Environment and CUSTOMER
```





## Contributing
Contributions to KOT Secret are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
KOT Secret is released under the MIT License.

<h2 align="center">
    Contributors
</h2>
<p align="center">
    Thank you for your contribution!
</p>
<p align="center">
    <a href="https://github.com/KOT-database/KOT-Secret/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=KOT-database/KOT-Secret" />
    </a>
</p>
