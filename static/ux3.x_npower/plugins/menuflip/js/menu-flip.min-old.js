jQuery(document).ready(function($) {
    var clickStatus = 0;
    var main_menu = $('.show-menu'),
        foldingPanel = $('.cd-folding-panel'),
        close_main_menu = $('#menuOverlay'),
        mainContent = $('#menu-wrapper'),
        menu_list = ['index.html', 'form_controls.html', 'date_time_pickers.html', 'fileupload.html',
            'tables.html', 'tabs_accordions.html', 'vertical_form_wizard.html', 'talent-matrix.html', 'charts.html','editor.html','kanban.html'
        ];

    /* open folding content */
    /* Open folding with hover */
    main_menu.mouseover(function(event) {
        clickStatus = 1;
        // event.preventDefault();
        if ($('.fold-is-open').length > 0) {
            toggleContent('', false);
        } else {
            openItemInfo();
        }
    });
    /* Open folding with click */
    //	main_menu.on('click', function(event){
    //		clickStatus = 1;
    //		event.preventDefault();
    //		if ( $('.fold-is-open').length > 0) {
    //			toggleContent('', false);
    //		} else {
    //			openItemInfo();
    //		}
    //	});

    /* close folding content */
    /* Close folding with hover */
    //    main_menu.mouseout(function(event) {
    //      event.preventDefault();
    //		if(clickStatus == 1){
    //			toggleContent('', false);
    //        		$("#menu-ul").removeClass("important1 blue1");
    //			$(".menu-li").removeClass("important menu-li-expand");
    //			$("#menu-ul").hide();
    //			$('.show-menu').show();
    //			$(".gt-dev").show();
    //		}
    //    });
    /* Close folding with click */
    close_main_menu.on('click', function(event) {
        // event.preventDefault();
        if (clickStatus == 1) {
            toggleContent('', false);
            $("#menu-ul").removeClass("important1 blue1");
            $(".menu-li").removeClass("important menu-li-expand");
            $("#menu-ul").hide();
            $('.show-menu').show();
            $(".gt-dev").show();
        }
    });

    function openItemInfo() {
        toggleContent(true);
    }

    function toggleContent(bool) {
        if (bool) {
            /* load and show new content */
            setTimeout(function() {
                foldingPanel.addClass('is-open');
                mainContent.addClass('fold-is-open');
            }, 100);
            $(".menu-li").removeAttr('style')
            $("#menu-ul").removeAttr('style')
            var menu_count = $(".menu-li").length;
            var menu_space = parseInt((360 / menu_count).toFixed());
            var temp_menu_space = 0;
            if (menu_count > 4) {
                for (var i = 0; i < menu_count; i++) {
                    rotate_position = i + 1
                    if (i == 0) {
                        $("#menu-ul > .i" + rotate_position).css({
                            'transform': 'translateZ(200px)',
                            '-moz-transform': 'translateZ(200px)',
                            '-o-transform': 'translateZ(200px)',
                            '-ms-transform': 'translateZ(200px)',
                            '-webkit-transform': 'translateZ(200px)'
                        });
                    } else {
                        temp_menu_space = menu_space + temp_menu_space;
                        $("#menu-ul > .i" + rotate_position).css({
                            'transform': 'rotateY(' + temp_menu_space + 'deg) translateZ(200px)',
                            '-moz-transform': 'rotateY(' + temp_menu_space + 'deg) translateZ(200px)',
                            '-o-transform': 'rotateY(' + temp_menu_space + 'deg) translateZ(200px)',
                            '-ms-transform': 'rotateY(' + temp_menu_space + 'deg) translateZ(200px)',
                            '-webkit-transform': 'rotateY(' + temp_menu_space + 'deg) translateZ(200px)'
                        });
                    }
                }
            } else {
                $(".menu-li").addClass("menu-li-expand").removeAttr('style').css({
                    'position': 'static',
                    'transform': 'none !important',
                    'display': 'inline-block'
                });
                $("#menu-ul").addClass("important1 blue1");
            }
            $("#menu-ul").show();
            $(".gt-dev").hide();
        } else {
            /* close the folding panel */
            foldingPanel.removeClass('is-open');
            mainContent.removeClass('fold-is-open');
        }
    }

    $(".menu-li").click(function(event) {
        if ($(".menu-li-expand").length == 0) {
            event.preventDefault();
            var li_count = $("#menu-ul").children('li').length;
            for (var i = 1; i <= li_count; i++) {
                //$("#menu-ul > .i" + i).find("a").removeAttr("href");
            //    $("#menu-ul > .i" + i).find("a").attr("href", menu_list[i-1]);
            }
            $(".menu-li").addClass("menu-li-expand").removeAttr('style').css({
                'position': 'static',
                'transform': 'none !important',
                'display': 'inline-block'
            });
            $("#menu-ul").addClass("important1 blue1");
        } 
    });
   
    /* First sub menu hover function */
    $('#menu-ul > li').hover(function() {
        if ($(".menu-li-expand").length > 0) {
            if ($('> ul.sub-menu', this).length > 0) {
                $('> ul.sub-menu', this).css({
                    'visibility': 'visible',
                    'transform': 'scaleY(1)'
                });
            }
        }
    }, function() {
        if ($(".menu-li-expand").length > 0) {
            if ($('> ul.sub-menu', this).length > 0) {
                $('> ul.sub-menu', this).css({
                    'visibility': '',
                    'transform': ''
                });
            }
        }
    });

    /* Second sub menu hover function */
    $('.sub-menu > li').hover(function() {
        var curr_pos_li = $(this).index(),
            first_sub_menu_count = $(this).parent('ul').children('li').length,
            second_sub_menu_count = $(this).find('ul.second-sub-menu').children('li').length,
            diff_sub_lis = Math.abs(curr_pos_li - first_sub_menu_count);
        if (diff_sub_lis >= 3) {
            if (second_sub_menu_count >= first_sub_menu_count) {
                $(this).find('ul.second-sub-menu').css({
                    'visibility': 'visible',
                    'transform': 'scaleY(1)',
                    'bottom': '0px',
                    'top': 'inherit'
                });
            } else {
                $(this).find('ul.second-sub-menu').css({
                    'visibility': 'visible',
                    'transform': 'scaleY(1)'
                });
            }
        } else {
            $(this).find('ul.second-sub-menu').css({
                'visibility': 'visible',
                'transform': 'scaleY(1)',
                'bottom': '0px',
                'top': 'inherit'
            });
        }
    }, function() {
        var curr_pos_li = $(this).index() + 1,
            first_sub_menu_count = $(this).parent('ul').children('li').length,
            second_sub_menu_count = $(this).find('ul.second-sub-menu').children('li').length,
            diff_sub_lis = Math.abs(curr_pos_li - first_sub_menu_count);
        if (diff_sub_lis >= 3) {
            if (second_sub_menu_count >= first_sub_menu_count) {
                $(this).find('ul.second-sub-menu').css({
                    'visibility': '',
                    'transform': '',
                    'bottom': '',
                    'top': ''
                });
            } else {
                $(this).find('ul.second-sub-menu').css({
                    'visibility': '',
                    'transform': ''
                });
            }
        } else {
            $(this).find('ul.second-sub-menu').css({
                'visibility': '',
                'transform': '',
                'bottom': '',
                'top': ''
            });
        }
    });
});