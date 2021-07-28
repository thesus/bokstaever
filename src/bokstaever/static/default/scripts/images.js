const NEXT_TYPE = {
  IMAGE: 0,
  PAGE: 1,
  NONE: 2
}

function getElements(elements) {
  let result = {}
  for (let element of elements) {
    result[element] = document.getElementById(element)
  }
  return result
}

class ImageFeed {
  constructor () {
    this.currentPage = 1
    this.lastPage = null
    this.images = []

    this.nextEventFunction = null
    this.prevEventFunction = null


    this.elements = getElements([
      "buttonPrevPage",
      "buttonNextPage",
      "images",
      "modal",
      "modalContent",
      "modalClose",
      "modalFooter",
      "imageName",
      "imageDate",
      "buttonNextImage",
      "buttonPrevImage"
    ])

    this.setupNavigation()
    this.setupModal()
    this.getImages(1)
  }

  setupNavigation() {
    this.elements.buttonPrevPage.addEventListener("click", this.navigationClosure(-1).bind(this))
    this.elements.buttonNextPage.addEventListener("click", this.navigationClosure(1).bind(this))
  }

  closeModal() {
    this.elements.modal.className = "modal"
  }

  // Add eventlisteners to modal background and close button
  setupModal() {
    this.elements.modal.addEventListener("click", function(event) {
      if (this.elements.modal === event.target) {
        this.closeModal()
      }
    }.bind(this))

    this.elements.modalClose.addEventListener("click", function(event) {
      this.closeModal()
    }.bind(this))

    // On mobile devices we want to hide the prev/next buttons on a click on the mobile
    this.elements.modalContent.addEventListener("click", (event) => {
      if (this.elements.modalContent.className.endsWith(" clicked")) {
        let classes = this.elements.modalContent.className
        this.elements.modalContent.className = classes.substring(0, classes.length - 8)
      } else {
        this.elements.modalContent.className += " clicked"
      }
    })
  }

  // Download images
  async getImages(page) {
    this.currentPage = page

    let response;
    try {
      response = await fetch(`/api/images/?page=${this.currentPage}&detailed`)
    } catch (error) {
      // Could happen on an network error
      this.showError("Ein Fehler ist aufgetreten. Ist das Netzwerk erreichbar?")
    }

    if (response.status !== 200) {
      this.showError(`Etwas ist schief gelaufen... ${response.status}`)
      return
    }

    const data = await response.json()
    this.lastPage = data.pages

    this.images = data.result;

    this.updateNavigation()
    this.updateImageList()
  }

  navigationClosure(amount) {
    return function(event) {
      this.getImages(this.currentPage + amount)
    }
  }

  imageSelectClosure(image) {
    return async function(event) {
      this.setOpen(image)

      await new Promise(resolve => setTimeout(resolve, 100))
      this.elements.modal.className = "modal show"
    }
  }

  // Open modal and display enlarged image
  setOpen(image) {
    const element = document.createElement("img")

    let srcset = ""
    for (const file of image[2]) {
      srcset += `${file[2]} ${file[0]}w, `
    }

    element.srcset = srcset
    element.src = image[2][0][2]

    // Replace an existing image with a new one
    if (this.elements.modalContent.firstChild.nodeName === "IMG") {
      this.elements.modalContent.removeChild(this.elements.modalContent.firstChild)
    }

    this.elements.imageName.textContent = image[3]
    this.elements.imageDate.textContent = (new Date(image[4])).toLocaleString()

    this.elements.modalContent.prepend(element)

    // Setup the next button
    const nextImage = this.imageHasNext(image);
    const hasNext = nextImage != NEXT_TYPE.NONE;
    this.elements.buttonNextImage.disabled = !hasNext;

    if (this.nextEventFunction) {
      this.elements.buttonNextImage.removeEventListener("click", this.nextEventFunction);
    }

    if (hasNext) {
      this.nextEventFunction = async function(event) {
          if (nextImage === NEXT_TYPE.IMAGE) {
            this.setOpen(this.images[this.images.indexOf(image) + 1])
          } else {
            await this.getImages(this.currentPage + 1);
            this.setOpen(this.images[0]);
          }
      }.bind(this)

      this.elements.buttonNextImage.addEventListener("click", this.nextEventFunction)
    } else {
      this.nextEventFunction = null;
    }


    // setup the previous button
    const prevImage = this.imageHasPrev(image);
    const hasPrev = prevImage != NEXT_TYPE.NONE;
    this.elements.buttonPrevImage.disabled = !hasPrev;

    if (this.prevEventFunction) {
      this.elements.buttonPrevImage.removeEventListener("click", this.prevEventFunction);
    }

    if (hasPrev) {
      this.prevEventFunction = async function(event) {
          if (prevImage === NEXT_TYPE.IMAGE) {
            this.setOpen(this.images[this.images.indexOf(image) - 1])
          } else {
            await this.getImages(this.currentPage - 1);
            this.setOpen(this.images[this.images.length - 1]);
          }
      }.bind(this)

      this.elements.buttonPrevImage.addEventListener("click", this.prevEventFunction)
    } else {
      this.prevEventFunction = null;
    }
  }

  // Updates state of navigation buttons (disabling)
  updateNavigation() {
    if (this.currentPage > 1) {
      this.elements.buttonPrevPage.disabled = false
    } else {
      this.elements.buttonPrevPage.disabled = true
    }

    if (this.currentPage < this.lastPage) {
      this.elements.buttonNextPage.disabled = false
    } else {
      this.elements.buttonNextPage.disabled = true
    }
  }

  imageHasNext(image) {
    if (this.images.indexOf(image) < this.images.length - 1) {
      return NEXT_TYPE.IMAGE
    } else if (this.currentPage < this.lastPage) {
      return NEXT_TYPE.PAGE
    } else {
      return NEXT_TYPE.NONE
    }
  }

  imageHasPrev(image) {
    if (this.images.indexOf(image) > 0) {
      return NEXT_TYPE.IMAGE
    } else if (this.currentPage > 1) {
      return NEXT_TYPE.PAGE
    } else {
      return NEXT_TYPE.NONE
    }
  }

  // Updates image list in DOM
  updateImageList() {
    const anchor = document.createElement("div")
    anchor.className = "images"

    for (const image of this.images) {
      let imageElement = document.createElement("img")
      imageElement.src = image[1]
      imageElement.addEventListener(
        "click",
        this.imageSelectClosure(image).bind(this)
      )

      anchor.appendChild(imageElement)
    }

    // Append assembled images at the end
    this.elements.images.textContent = ""
    this.elements.images.appendChild(anchor)
  }

  // Displays the given error message and clears all images
  showError(message) {
    const errorElement = document.createElement("span")
    errorElement.textContent = message

    this.elements.images.textContent = ""
    this.elements.images.appendChild(errorElement)
  }
}

const feed = new ImageFeed()

