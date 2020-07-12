function createElement(type, classes) {
  let element = document.createElement(type)
  element.className = classes
  return element
}

class ImageUpload {
  constructor (uploadURL) {
    this.uploadURL = uploadURL

    this.form = document.getElementById("imageUpload")
    this.imageInput = document.getElementById("imageInput")
    this.anchor = document.getElementById("anchor")
    this.trigger = document.getElementById("trigger")
    this.alert = document.getElementById("alertAnchor")

    this.csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value

    // Images extracted from the multi file input
    this.images = []
    // Amount of images loading, used for actions once after finishing all uploads
    this.loading = 0
    // Encodes if there was an error on any upload
    this.wasError = false

    // Uploads the images to the server
    this.trigger.onclick = this.uploadImages.bind(this)

    // Updates `this.images` if the input changes
    this.imageInput.onchange = this.updateImages.bind(this)
  }

  // Closes all alerts on the alert anchor
  clearAlert() {
    for (let node of this.alert.childNodes) {
      let alert = new bootstrap.Alert(this.alert.firstChild)
      alert.close()
      node.addEventListener("closed.bs.alert", function() {
        this.alert.removeChild(node)
      })
    }
  }

  // Appends a alert with the given message to the alert anchor
  displayError(message) {
    let alert = createElement("div", "alert alert-danger alert-dismissible fade show")
    alert.setAttribute("role", "alert")

    let content = document.createElement("span")
    content.appendChild( document.createTextNode(message) )
    alert.appendChild(content)

    let button = createElement("button", "close")
    button.type = "button"
    button.setAttribute("data-dismiss", "alert")
    button.setAttribute("aria-label", "close")

    let span = document.createElement("span")
    span.setAttribute("aria-hidden", true)
    span.innerHTML = "&times;"

    button.appendChild(span)
    alert.appendChild(button)

    this.alert.appendChild(alert)
  }

  // Changes visibility of the progress bar of a given image
  toggleProgress(id) {
    let node = this.images[id].node.lastChild.lastChild.lastChild

    if (node.style.display !== "none") {
      node.style.display = "none"
    } else {
      node.style.display = "flex"
    }
  }

  // Resets the progress bar to 0
  resetProgress(id) {
    let node = this.images[id].node.lastChild.lastChild.lastChild.lastChild

    // If reenabled set to start
    node.style.width = 0
    node.setAttribute("aria-valuenow", 0)
  }

  // Disables the input on a given image
  disableInput(id, on) {
    let node = this.images[id].node.lastChild.lastChild.firstChild
    node.disabled = on
  }

  // Disables the upload button
  disableSubmit(on) {
    this.trigger.disabled = on
  }

  uploadImages() {
    // count how many requests will be made to the server
    this.loading = this.images.filter((image) => { return (image.success === null || image.success === false) }).length
    // reset previous error state
    this.wasError = false
    // Allow pressing upload only once
    this.disableSubmit(true)
    // reset alert state
    this.clearAlert()

    for (const [index, image] of this.images.entries()) {
      if (image.success === null || image.success === false) {
        if (image.success === false) {
          // Reset the error lining on previously failed images
          image.node.className = "card"
        } else {
          // Enable progress bar on the given image on the first try
          this.toggleProgress(index)
        }

        // Disable inputs during upload
        this.disableInput(index, true)

        let data = new FormData()
        data.append("image", image.file)
        data.append("title", image.title)
        data.append("csrfmiddlewaretoken", this.csrf_token)

        let xhr = new XMLHttpRequest();

        xhr.responseType = "json"

        xhr.upload.addEventListener("progress", this.updateProgressFunction(index).bind(this))

        // Update the image on load and error events
        xhr.addEventListener("load", this.updateImageFunction(index).bind(this))
        xhr.addEventListener("error", this.updateImageFunction(index).bind(this))

        xhr.open("POST", this.uploadURL)
        xhr.send(data)
      }
    }
  }

  // Updates the internal representation via the event listener during upload
  updateImageFunction(id) {
    return function (event) {
      let status = event.target.status === 200
      this.images[id].success = status
      // one image less is loading
      this.loading--

      if (status) {
        // set green card lining on success
        this.images[id].node.className = "card border-success"
      } else {
        // reset progress and enable input for next attempt
        this.resetProgress(id)
        this.disableInput(id, false)
        this.wasError = true

        // set red card lining on failure
        this.images[id].node.className = "card border-danger"
      }

      // if all images are loaded and there was an error, show alert and reenable the upload button
      if (this.wasError && this.loading === 0) {
        this.displayError("An error occured. You may try to upload again.")
        this.disableSubmit(false)
      } else if (this.loading === 0) {
        // All images loaded successfully. Return to overview
        document.location.href = "/dashboard/images"
      }
    }
  }

  // update the progress for a given image
  updateProgressFunction(id) {
    return function (event) {
      let node = this.images[id].node.lastChild.lastChild.lastChild.lastChild
      let value = Math.round((event.loaded / event.total) * 100)

      node.setAttribute("aria-valuenow", value)
      node.style.width = `${value}%`
    }
  }

  // change the internal image title if the input changes
  updateTitleFunction(id) {
    return function (event) {
      this.images[id].title = event.target.value
    }
  }

  // Reads the images from the input
  updateImages() {
    this.images = []

    const files = this.imageInput.files

    for (let image of files) {
      let name = image.name
      // title is propably the part before the last dot
      let title = name.substring(0, name.lastIndexOf('.'))

      this.images.push({
        'title': title,
        'file': image,
        'url': URL.createObjectURL(image),
        'success': null,
        'node': null
      })
    }

    // if there are (new) images enable the upload button
    this.disableSubmit(this.images.length === 0)

    this.updateDOM()
  }

  // creates the image cards after creating the internal representation
  updateDOM() {
    // Clear old images
    anchor.textContent = ""

    for (const [index, image] of this.images.entries()) {
      let card = createElement("div", "card")
      card.style.width = 180

      // create Progressbar as last child
      let progress = createElement("div", "progress")
      progress.style.display = "none"
      let progressBar = createElement("div", "progress-bar")
      progressBar.setAttribute("role", "progressbar")
      // Accessibility
      progressBar.setAttribute("aria-valuenow", 0)
      progressBar.setAttribute("aria-valuemin", 0)
      progressBar.setAttribute("aria-valuemax", 100)
      progress.appendChild(progressBar)

      // Add the image
      let img = createElement('img', "card-img-top")
      img.src = image.url

      let cardBody = createElement("div", "card-body")
      let cardText = createElement("div", "card-text")

      let input = createElement("input", "form-control")
      input.value = image.title
      input.required = true
      input.addEventListener("input", this.updateTitleFunction(index).bind(this))

      anchor.appendChild(card)
      image['node'] = card

      card.appendChild(img)
      card.appendChild(cardBody)
      cardBody.appendChild(cardText)
      cardText.appendChild(input)
      cardText.appendChild(progress)
    }
  }
}
