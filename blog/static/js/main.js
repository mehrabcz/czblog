(function($){

	"use strict";

	var Sasha = {

      // Bootstrap Carousels

      carousel: function() {

      	$('.carousel.slide').carousel({
      		cycle: true
      	}); 
      }, 

      matchHeight: function() {
      	$('article.post.type-post, .widget_instagram_feed img').matchHeight({ 
      		property: 'min-height' 
      	});

      },

		// Owl Carousels 

		owlcarousel: function() {
			try { 
				(function($) {

					$(".banner-slider-02").owlCarousel({
						items:2,
						loop:true,
						margin:3,
						nav: false,
						autoplay: true,
						responsive:{
							320:{
								items:1
							},
							436:{
								items:1
							},
							480:{
								items:2
							}
						}
					});

					$(".banner-slider-05").owlCarousel({
						items:2,
						loop:true,
						center: true,
						margin:20,
						nav: false,
						autoplay: true,
						responsive:{
							320:{
								items:1
							},
							436:{
								items:1
							},
							480:{
								items:2
							}
						}
					});

				})(jQuery);
			} catch(e) { 

			} 
		},

		// Isotop Filters

		isotope: function() {

			var $PortfolioItems = $('.masonry-posts');
			$PortfolioItems.isotope({
				itemSelector: 'article',
				layoutMode: 'masonry',
				transitionDuration: '0.6s',
				percentPosition: true,
				margin: 45,
				masonry: {
					columnWidth: 'article'
				}

			});
		},


		// Images Loaded

		imagesloaded: function() {

			var $PortfolioItems = $('.masonry-posts');
			$PortfolioItems.imagesLoaded().progress( function() {
				$PortfolioItems.isotope('layout');
			});  
		},

	};


	$(document).ready(function() {
		"use strict";

		// Background Img

		$(".background-bg").css('background-image', function () {
			var bg = ('url(' + $(this).data("image-src") + ')');
			return bg;
		});

		$('.form-trigger').on('click', function(event) {
			event.preventDefault(); 
			event.stopPropagation(); 
			$(this).parent().toggleClass('open');
		});

		$('.form-trigger').on('click', function(event) {
			event.preventDefault(); 
			event.stopPropagation(); 
			$(this).parent().siblings().removeClass('open');
		});

		// Sidebar Nav Open / Close	

		$('.side-menu-trigger').on('click', function() {
			$('.overlay-wrapper').toggleClass('open');
		});

		$('.menu-close').on('click', function(event) {
			$('.overlay-wrapper').removeClass('open');
		});

		// Sidebar Menu Dropdown Open / Close	

		$('.sidebar-menu .menu-item-has-children>a').on('click', function(event) {
			event.preventDefault(); 
			event.stopPropagation(); 
			$(this).parent().siblings().removeClass('open');
			$(this).parent().toggleClass('open');
		});



		Sasha.carousel();
		Sasha.matchHeight();
		Sasha.owlcarousel();
		Sasha.isotope();
		Sasha.imagesloaded();
	});


	// Responsive Menu Open and Close in Mobile

	if ($(window).width() < 767) {
		"use strict";
		$('#main-menu .menu-item-has-children>a').on('click', function(event) {
			event.preventDefault(); 
			event.stopPropagation(); 
			$(this).parent().siblings().removeClass('open');
			$(this).parent().toggleClass('open');
		});
		
	};


	jQuery(window).on('scroll', function () {
		
		'use strict';

		if (jQuery(this).scrollTop() > 100) {
			jQuery('#scroll-to-top').fadeIn('slow');
		} else {
			jQuery('#scroll-to-top').fadeOut('slow');
		}

	});


	jQuery('#scroll-to-top').on("click", function() {
		
		'use strict';

		jQuery("html,body").animate({ scrollTop: 0 }, 1500);
		return false;
	});



})(jQuery);




