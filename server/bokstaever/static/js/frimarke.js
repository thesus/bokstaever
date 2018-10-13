var msnry

var breakpoint = 760

var grid = document.querySelector('.posts')

function createMasonry (grid) {
  return new Masonry( grid, {
    itemSelector: '.post',
    columnWidth: 350,
    gutter: 25,
    fitWidth: true
  }) 
}

if (window.innerWidth > breakpoint) {
  msnry = createMasonry(grid)
} else {
  msnry = undefined
}

function checkMasonry () {
  let width = window.innerWidth
  if (width <= breakpoint) {
    if (msnry != undefined) {
      // console.log('destroying msnry')
      msnry.destroy()
      msnry = undefined
    }
  } else {
    if (msnry === undefined) {
      // console.log('creating msnry')
      msnry = createMasonry(grid)
    }
  }
}

window.addEventListener('resize', checkMasonry)

imagesLoaded(grid).on( 'progress', function() {
  if (msnry) {
    msnry.layout()
  }  
})
