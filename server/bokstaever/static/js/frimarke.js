var grid = document.querySelector('.posts');

var msnry = new Masonry( grid, {
  itemSelector: '.post',
  columnWidth: 350,
  gutter: 25,
  fitWidth: true
});

imagesLoaded(grid).on( 'progress', function() {
  msnry.layout()
})
