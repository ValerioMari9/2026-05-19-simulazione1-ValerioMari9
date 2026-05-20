from dataclasses import dataclass
@dataclass
class Artist:
    ArtistId: int
    Name: str
    def __eq__(self, other):
        return self.ArtistId==other.ArtistID
    def __hash__(self):
        return hash(self.ArtistId)