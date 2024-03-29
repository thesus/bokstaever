class ImageSelectWidget {
  constructor(idPrefix, multiple, images, text) {
    this.text = text

    this.idPrefix = idPrefix

    this.multiple = multiple
    this.images = images

    this.page = 1
    this.max = null

    this.anchor = document.getElementById(idPrefix + 'Images')
    this.buttonPrevious = document.getElementById(idPrefix + 'ButtonPrevious')
    this.buttonNext = document.getElementById(idPrefix + 'ButtonNext')
    this.modal = document.getElementById(idPrefix + 'Modal')


    // Navigation inside the modal
    this.buttonPrevious.addEventListener("click", function () {
      if (this.page > 1) {
        this.page--
        this.getImages()
      }
    }.bind(this))

    this.buttonNext.addEventListener("click", function () {
      if (this.page < this.max) {
        this.page++
        this.getImages()
      }
    }.bind(this))

    // update the hidden input with the selected images
    if (this.multiple) {
      this.updateInputMultiple()
    }
  }

  updateInputMultiple() {
    const hiddenInput = document.getElementById("id_" + this.idPrefix)

    // Set the input to a list of images
    hiddenInput.value = Array.from(this.images).join(",")
  }

  selectFunction(image) {
    return function (event) {
      const selected = document.getElementById(this.idPrefix + 'Selected').firstChild

      if (this.multiple) {
        if (this.images.has(image[0])) {
          this.images.delete(image[0])

          // if the image was previously highlighted, remove highlight
          event.target.className = "img-thumbnail selectable"
        } else {
          this.images.add(
            image[0]
          )

          // Highlight images that are selected
          event.target.className = "img-thumbnail border-primary selected selectable"
        }

        this.updateInputMultiple()
        selected.textContent = this.images.size + this.text.count
      } else {
        const hiddenInput = document.getElementById("id_" + this.idPrefix)

        selected.className = "small-thumbnail img-thumbnail"
        selected.src = image[1]

        // Set the input to a single image
        hiddenInput.value = image[0]
      }
    }
  }

  // Fetches images and creates the thumnails in the modal
  async getImages() {
    this.anchor.textContent = ""

    const response = await fetch(`/api/images/?page=${this.page}&all`)
    const data = await response.json()

    // Update max count
    this.max = data.pages

    if (data.current > 1) {
      this.buttonPrevious.className = "page-item"
      this.buttonPrevious.firstChild.disabled = false
    } else {
      this.buttonPrevious.className = "page-item disabled"
      this.buttonPrevious.firstChild.disabled = true
    }

    if (data.current < this.max) {
      this.buttonNext.className = "page-item"
      this.buttonNext.firstChild.disabled = false
    } else {
      this.buttonNext.className = "page-item disabled"
      this.buttonNext.firstChild.disabled = true
    }

    if (data.count === 0) {
      let element = document.createElement("span")
      element.appendChild(document.createTextNode(this.text.noImages))
      this.anchor.appendChild(element)
    }

    for (let image of data.result) {
      let col = document.createElement("div")
      col.className = "col-6 col-sm-4 col-lg-3"
      this.anchor.appendChild(col)

      let element = document.createElement("img")
      element.src = image[1]

      let classes = "img-thumbnail selectable"

      // Highlight the selected images
      if (this.multiple && this.images.has(image[0])) {
        classes += " border-primary selected"
      }

      element.className = classes
      element.id = this.idPrefix + "Image" + image[0]


      // If a thumbnail is clicked, close the modal on single mode
      if (!this.multiple) {
        element.setAttribute('data-bs-dismiss','modal')
      }

      element.addEventListener("click", this.selectFunction(image).bind(this))

      col.appendChild(element)
    }
  }
}
