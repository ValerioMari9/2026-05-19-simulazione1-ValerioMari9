from database.DB_connect import DBConnect
from model.genre import Genre
from model.artist import Artist
class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getGenres():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        q="""select * from genre;"""
        cursor.execute(q)
        l=cursor.fetchall()
        res=[Genre(**i) for i in l]
        cursor.close()
        cnx.close()
        return res
    @staticmethod
    def getArtists():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        q="""select * from artist;"""
        cursor.execute(q)
        l=cursor.fetchall()
        res=[Artist(**i) for i in l]
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getArtistsFromGenre(gen: int):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        q = """select a.ArtistId, count(*) 
from track t, album a, invoiceline il  
where  il.TrackId = t.TrackId  and 
a.AlbumId = t.AlbumId and t.GenreId =%s
group by a.ArtistId ;
"""
        cursor.execute(q, (gen, ))
        l = cursor.fetchall()
        res = [i for i in l]
        cursor.close()
        cnx.close()
        return res
    @staticmethod
    def getEdges(gen: int):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        q = """select distinctrow t2.art, t1.art	
from (select a.ArtistId as art, i.CustomerId as cus 
from invoice i, invoiceline il, track t, album a
where i.InvoiceId = il.InvoiceId and 
	il.TrackId = t.TrackId and a.AlbumId = t.AlbumId and t.GenreId = %s) t1, (select a.ArtistId as art, i.CustomerId as cus 
from invoice i, invoiceline il, track t, album a
where i.InvoiceId = il.InvoiceId and 
	il.TrackId = t.TrackId and a.AlbumId = t.AlbumId and t.GenreId = %s) t2
where t2.cus = t1. cus and t1.art< t2.art;
        """
        cursor.execute(q, (gen,gen))
        l = cursor.fetchall()
        res = [i for i in l]
        cursor.close()
        cnx.close()
        return res





