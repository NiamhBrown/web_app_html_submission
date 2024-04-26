from playwright.sync_api import Page, expect

def test_return_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    para_tags = page.locator("p")
    expect(h2_tags).to_have_text(["title1", "title2"])
    expect(para_tags).to_have_text(["Released: 1111", "Released: 2222"])

def test_return_an_album_with_id(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h2_tags = page.locator("h2")
    para_tags = page.locator("p")
    expect(h2_tags).to_have_text(["title1"])
    expect(para_tags).to_have_text(["Released: 1111"])

# def test_add_artist(web_client, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post('/artists', data = {'name':'David', 'genre':'pop'})
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == 'David has been added as an artist!'

#     get_response = web_client.get('/artists')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "[Artist(1, Pixies, Rock), Artist(2, ABBA, Pop), Artist(3, Taylor Swift, Pop), Artist(4, Nina Simone, Jazz), Artist(5, David, pop)]"



