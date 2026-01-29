
def build_tmdb_filters(request):

    params = []

    genre_ids = request.GET.getlist('genre')
    year = request.GET.get('year')
    rating = request.GET.get('rating')
    page = request.GET.get('page', 1)

    if genre_ids:
        params['with_genres'] = ','.join(genre_ids)

    if year:
        params['primary_release_year'] = year

    if rating:
        params['vote_average.gte'] = rating

    params['page'] = page

    return params