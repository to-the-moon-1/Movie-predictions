$(document).ready(function () {
        const predict_btn = $('button[class="btn btn-warning predict_btn"]');
        const back_btn = $('button[class="btn btn-light tab position"]');
        const next_btn = $('button[class="btn btn-warning tab position"]');

        $('#predict').click(function () {
            const movie_name = $('#id_name');
            const movie_genre = $('#id_genre');
            const movie_actors_0 = $('#id_actors_0');
            const movie_actors_1 = $('#id_actors_1');
            const movie_imdb = $('#id_imdb');

            const movie_metascore = $('#id_metascore').val();
            const movie_user_score = $('#id_user_score').val();
            const movie_tomatometer = $('#id_tomatometer').val();
            const movie_audience_score = $('#id_audience_score').val();
            const movie_liked_this_film = $('#id_liked_this_film').val();
            const movie_audience_rating_summary = $('#id_audience_rating_summary').val();

            if (((movie_metascore !== '' && movie_metascore <= 100) && (movie_user_score !== '' && movie_user_score <= 10) && (movie_tomatometer !== '' && movie_tomatometer <= 100) && (movie_audience_score !== '' && movie_audience_score <= 100) && (movie_liked_this_film !== '' && movie_liked_this_film <= 100) && (movie_audience_rating_summary !== '' && movie_audience_rating_summary <= 5)) && (movie_name.val() === '' || movie_genre.val().length === 0 || (movie_actors_0.is(':checked') === false || movie_actors_1.is(':checked') === false) || movie_imdb.val() !== '' || movie_imdb.val() > 10)) {
                movie_name.attr('required', 'true');
                movie_genre.attr('required', 'true');
                movie_actors_0.attr('required', 'true');
                movie_actors_1.attr('required', 'true');
                movie_imdb.attr('required', 'true');

                predict_btn.css('display', 'none');

                const tab = $('div[class="tab_content"]');

                tab.eq(1).removeClass('active_tab');
                tab.eq(0).addClass('active_tab');

                next_btn.removeClass('active');
                back_btn.addClass('active');

                $('.main_content .tab').addClass('active').eq($(this).index()).removeClass('active');
                $('.tab_content').show().eq($(this).index()).remove('active_tab').fadeOut(0);
            }
        })

        $('selectpicker').selectpicker();

        $('label:not([for])').attr('for', 'id_actors');

        $('#id_actors').addClass('custom-control custom-radio').insertAfter('label[for="id_actors"]');
        $('#id_actors_0, #id_actors_1').addClass('custom-control-input');
        $('label[for="id_actors_0"], label[for="id_actors_1"]').addClass('custom-control-label');
        $('#id_actors_0').insertBefore('label[for="id_actors_0"]');
        $('#id_actors_1').insertBefore('label[for="id_actors_1"]');

        const paragraph = $('p');

        paragraph.slice(0, 6).wrapAll('<div class="tab_content first_tab"></div>');
        paragraph.slice(6, 14).wrapAll('<div class="tab_content second_tab"></div>');

        paragraph.eq(4).remove();

        $('.main_content .tab').click(function () {
            const movie_name = $('#id_name');
            const movie_genre = $('#id_genre');
            const movie_actors_0 = $('#id_actors_0');
            const movie_actors_1 = $('#id_actors_1');
            const movie_imdb = $('#id_imdb');

            if (back_btn.hasClass('active')) {
                predict_btn.css('display', 'inline-block');

                movie_name.removeAttr('required');
                movie_genre.removeAttr('required');
                movie_actors_0.removeAttr('required');
                movie_actors_1.removeAttr('required');
                movie_imdb.removeAttr('required');
            } else {
                predict_btn.css('display', 'none');

                movie_name.attr('required', 'true');
                movie_genre.attr('required', 'true');
                movie_actors_0.attr('required', 'true');
                movie_actors_1.attr('required', 'true');
                movie_imdb.attr('required', 'true');
            }

            $('.main_content .tab').removeClass('active').eq($(this).index()).addClass('active');
            $('.tab_content').hide().removeClass('active_tab').eq($(this).index()).addClass('active_tab').fadeIn(200)
        }).eq(0).addClass('active');
    }
);