
from __future__ import annotations

from typing import List
from xml.etree import ElementTree


class Movie:
    def __init__(
        self,
        title: str,
        format: str,
        year: int,
        rating: str,
        description: str,
        category: str,
    ):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category

    @classmethod
    def from_xml(cls, path: str) -> List[Movie]:
        tree = ElementTree.parse(path)
        movie_xml_file = tree.getroot()
        info_box = []
        movies = []
        for genr in movie_xml_file.iter("genre"):
            for mov in genr.iter('movie'):
                for child_tag in mov:
                    info_box.append(child_tag)
                movies.append(cls(mov.attrib["title"],
                    info_box[0],
                    info_box[1],
                    info_box[2],
                    info_box[3],
                    genr.attrib['category']
                    ))
                del info_box[:]
        return movies



if __name__ == '__main__':
    movies_list = Movie.from_xml("movie.xml")
    print(len(movies_list))


