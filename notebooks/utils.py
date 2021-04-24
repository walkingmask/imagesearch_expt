import io
from pathlib import Path
from typing import Optional
from typing import Union
import urllib.request

from PIL import Image
from PIL.Image import Image as PILImage


class ImageLoader:

    @staticmethod
    def load(location: Union[str, Path]) -> Optional[PILImage]:

        if isinstance(location, str):
            if location.startswith("http"):  # URL
                try:
                    return Image.open(
                        io.BytesIO(urllib.request.urlopen(location).read())
                    )
                except Exception as e:
                    print(f"Failed to load image from URL {location}")
                    print(e)
                    return None
            else:  # Local path
                location = Path(location)

        if isinstance(location, Path):  # Local path
            location = location.resolve()
            if location.exists():
                try:
                    return Image.open(str(location))
                except:
                    print(f"Failed to load image from path {location}")
                    return None
            else:
                print(f"Image file not found {location}")
                return None

        # Unexpected
        print(f"Unexpected type of image location {type(location)}")
        return None
