import random
import urllib


def make_it_burn(base_url: str, runs: int = 1_000):
    # test_paths = [
    #     "analyze_img?url=https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcShTBQ6O3Q5ICQHyg2jcEME65BYAbazSjJo6LEdhY50W7BkhoUDW9V1-oX80o8bSBgDeRdQhvDRm2jPGAnieBO4MezRanRqjZ1fbLJ8pqY",
    #     "analyze_img?url=https://apps.mpi.mb.ca/comms/drivershandbook/img/pedestrian.jpg",
    #     "analyze_img?url=https://www.driverseducationusa.com/drivers-ed-images/pedestrian-walk-car-waiting.jpg"
    #     "analyze_img?url=https://www.uab.edu/news/media/k2/items/cache/4bd9d6764ad7c49654f02ed2078e84c3_XL.jpg"
    # ]

    for i in range(0, runs):
        random_image_index = random.randint(0, 3)
        url = base_url + "analyze_img?path=C:\\Users\\Sebastian\\Downloads\\images.jpg"
        result = urllib.request.urlopen(url).read()

        print(f"Successfully enqueued a new job with id {result}")


if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000/"
    make_it_burn(base_url)
