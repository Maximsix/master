
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
                    info_box[0].text,
                    info_box[1].text,
                    info_box[2].text,
                    info_box[3].text,
                    genr.attrib['category']
                    ))
                del info_box[:]
        return movies

    def __str__(self):
        data = ""
        for key, value in self.__dict__.items():
            data += f"\t{key}: {value}\n"
        return f"{{\n{data[:len(data) - 1]}\n}}"



if __name__ == '__main__':
    for movie in Movie.from_xml("movie.xml"):
        print(movie)


