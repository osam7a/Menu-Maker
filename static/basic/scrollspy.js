$(document).ready(function() {
    'use strict';
  
    var $sections = $(".section");
    var sections = [];
  
    $sections.each(function() {
        sections.push({
            id: this.id,
            top: $(this).offset().top,
            height: $(this).outerHeight()
        });
    });
  
    $(window).on('scroll', function() {
        var scrollPosition = $(document).scrollTop();
        var windowHeight = $(window).height();
        var windowCenter = scrollPosition + windowHeight / 2;
        var currentSectionId = null;

        if (scrollPosition > 304) {
            $("#search-bar-container").removeClass("rounded-t-2xl");
        } else {
            $("#search-bar-container").addClass("rounded-t-2xl");
        }
  
        for (var i = 0; i < sections.length; i++) {
            var section = sections[i];
            if (section.top <= windowCenter && (section.top + section.height) > windowCenter) {
                currentSectionId = section.id;
                break;
            }
        }

        if (currentSectionId) {
            $('.active').removeClass('active');
            $('a[href*=' + currentSectionId + ']').addClass('active');
            // check if the section link in the horizontal navbar is visible
            var $sectionLink = $('a[href*=' + currentSectionId + ']');
            var $navbar = $("#sticky-nav"); // this is horizontal
            if ($sectionLink.length) {
                var navbarWidth = $navbar.width();
                var navbarScrollLeft = $navbar.scrollLeft();
                var sectionLinkOffset = $sectionLink.offset().left - $navbar.offset().left;
                var sectionLinkWidth = $sectionLink.width();
                var sectionLinkEnd = sectionLinkOffset + sectionLinkWidth;
                var navbarEnd = navbarScrollLeft + navbarWidth;
                var offset = 100; // add an offset of 100
                if (sectionLinkOffset < navbarScrollLeft) {
                    $navbar.scrollLeft(sectionLinkOffset - offset);
                } else if (sectionLinkEnd > navbarEnd) {
                    $navbar.scrollLeft(sectionLinkEnd - navbarWidth + offset);
                }
            }
        }
    });
});
