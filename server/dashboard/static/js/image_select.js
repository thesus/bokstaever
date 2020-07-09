class ImageSelectWidget {
  constructor(idPrefix) {
    this.idPrefix = idPrefix

    this.page = 1
    this.max = null

    this.anchor = document.getElementById(idPrefix + 'Images')
    this.buttonPrevious = document.getElementById(idPrefix + 'ButtonPrevious')
    this.buttonNext = document.getElementById(idPrefix + 'ButtonNext')

    this.modal = document.getElementById(idPrefix + 'Modal')

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
  }

  selectFunction(image) {
    return function () {
      const selected = document.getElementById(this.idPrefix + 'Selected')
      selected.className = "img-thumbnail"

      const hiddenInput = document.getElementById("id_" + this.idPrefix)

      selected.src = image[1]
      hiddenInput.value = image[0]
    }
  }

  async getImages() {
    this.anchor.textContent = ""

    const response = await fetch(`/api/images/?page=${this.page}`)
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
      element.appendChild(document.createTextNode("No images."))
      this.anchor.appendChild(element)
    }


    let index = 0;
    let row;
    for (let image of data.result) {
      // group in rows of three
      if (index % 3 === 0) {
        row = document.createElement("div")
        row.className = "row"

        this.anchor.appendChild(row)
      }

      let col = document.createElement("div")
      col.className = "col-sm-4"
      row.appendChild(col)

      let element = document.createElement("img")
      element.src = image[1]
      element.className = "img-thumbnail"
      element.id = this.idPrefix + "Image" + image[0]

      // If a thumbnail is clicked, close the modal
      element.setAttribute('data-dismiss','modal')
      element.addEventListener("click", this.selectFunction(image).bind(this))

      col.appendChild(element)

      index++
    }
  }
}
