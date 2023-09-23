# KOT Update

The cloud updating system for your python applications ! Control everything from one place and distribute all clients without effort

[Website](https://kotdatabase.dev/kot-update) | [Discord](https://discord.gg/QtnKf532Er) | [Twitter](https://twitter.com/kot_database)


[![Video](https://img.youtube.com/vi/WI8RVaSn278/0.jpg)](https://www.youtube.com/watch?v=WI8RVaSn278)


## Installation
You can install KOT by pip3:

```console
pip3 install kot_update
```


# Implementing
In this point you can use any [KOT Cloud](https://docs.kotdatabase.dev/kot_cloud.html).

```python
from kot_update import KOT_Update
from kot import KOT_Cloud
cloud = KOT_Cloud("YOUR_CLOUD_KEY")


updates = KOT_Update(cloud)

updates.pre_update("remove_lines") # Register your updates

# Define the updates
@cloud.active
def remove_lines(string):
    return string.replace("\n","")


updates.update() # Start to Update

```

And the console out is this:

```console
Updating: ['remove_lines']

remove_lines: OK

Updating Complated Without any Error
```




## Contributing
Contributions to KOT Update are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
KOT Update is released under the MIT License.

<h2 align="center">
    Contributors
</h2>
<p align="center">
    Thank you for your contribution!
</p>
<p align="center">
    <a href="https://github.com/KOT-database/KOT-Update/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=KOT-database/KOT-Update" />
    </a>
</p>
