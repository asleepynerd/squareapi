# squareify (dont hurt me ik it sucks)

simple api to squareify images it'll crop, or pad images to make them square.

you can just make a request using:

```bash
curl -F "file=@yourimage.jpg" http://localhost:5000/square --output squared.png
```

or

```bash
curl -F "url=https://example.com/image.jpg" http://localhost:5000/square --output squared.png
```

you can also specify the mode and size of the crop/pad using the following query params:

- `mode`: `top`, `right`, `bottom`, `left` (default: `center`)
- `size`: `256`, `512`, `1024` (default: `1024`)

```bash
curl -F "url=https://example.com/image.jpg" http://localhost:5000/square?mode=top&size=256 --output squared.png
```

ok thank you bye

btw i have an instance running at https://square.uwu.mba