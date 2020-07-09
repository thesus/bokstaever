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

    this.images = []
    this.loading = 0
    this.wasError = false

    this.trigger.onclick = this.uploadImages.bind(this)
    this.imageInput.onchange = this.updateImages.bind(this)
  }

  clearAlert() {
    for (let node of this.alert.childNodes) {
      let alert = new bootstrap.Alert(this.alert.firstChild)
      alert.close()
      node.addEventListener("closed.bs.alert", function() {
        this.alert.removeChild(node)
      })
    }
  }

  displayError(message) {
    let alert = document.createElement("div")
    alert.className = "alert alert-danger alert-dismissible fade show"
    alert.setAttribute("role", "alert")
    let content = document.createElement("span")
    content.appendChild( document.createTextNode(message) )
    alert.appendChild(content)

    let button = document.createElement("button")
    button.className = "close"
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

  toggleProgress(id) {
    let node = this.images[id].node.lastChild.lastChild.lastChild

    if (node.style.display !== "none") {
      node.style.display = "none"
    } else {
      node.style.display = "flex"
    }
  }

  resetProgress(id) {
    let node = this.images[id].node.lastChild.lastChild.lastChild.lastChild

    // If reenabled set to start
    node.style.width = 0
    node.setAttribute("aria-valuenow", 0)
  }

  toggleInput(id, on) {
    let node = this.images[id].node.lastChild.lastChild.firstChild
    node.disabled = on
  }

  disableSubmit(on) {
    this.trigger.disabled = on
  }

  uploadImages() {
    this.loading = this.images.filter((image) => { return (image.success === null || image.success === false) }).length
    this.wasError = false
    this.disableSubmit(true)
    this.clearAlert()

    for (const [index, image] of this.images.entries()) {
      if (image.success === null || image.success === false) {
        if (image.success === false) {
          image.node.className = "card"
        } else {
          // Enable progress bar on the given image
          this.toggleProgress(index)
        }

        this.toggleInput(index, true)

        let data = new FormData()
        data.append("image", image.file)
        data.append("title", image.title)
        data.append("csrfmiddlewaretoken", this.csrf_token)

        let xhr = new XMLHttpRequest();

        xhr.responseType = "json"

        xhr.upload.addEventListener("progress", this.updateProgressFunction(index).bind(this))

        xhr.addEventListener("load", this.updateImageFunction(index).bind(this))
        xhr.addEventListener("error", this.updateImageFunction(index).bind(this))

        xhr.open("POST", this.uploadURL)
        xhr.send(data)
      }
    }

    return false
  }

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

    this.disableSubmit(this.images.length === 0)

    this.updateDOM()
  }

  updateImageFunction(id) {
    return function (event) {
      let status = event.target.status === 200
      this.images[id].success = status
      this.loading--

      // this.toggleProgress(id)

      if (status) {
        this.images[id].node.className = "card border-success"
      } else {
        this.resetProgress(id)
        this.toggleInput(id, false)
        this.wasError = true

        this.images[id].node.className = "card border-danger"
      }

      if (this.wasError && this.loading === 0) {
        this.displayError("An error occured. You may try to upload again.")
        this.disableSubmit(false)
      }
    }
  }

  updateProgressFunction(id) {
    return function (event) {
      let node = this.images[id].node.lastChild.lastChild.lastChild.lastChild
      let value = Math.round((event.loaded / event.total) * 100)
      node.setAttribute("aria-valuenow", value)
      node.style.width = `${value}%`
    }
  }

  updateTitleFunction(id) {
    return function (event) {
      this.images[id].title = event.target.value
    }
  }

  updateDOM() {
    // Clear old images
    anchor.textContent = ""

    for (const [index, image] of this.images.entries()) {
      let card = createElement("div", "card")
      card.style.width = 180

      let progress = createElement("div", "progress")
      progress.style.display = "none"

      let progressBar = createElement("div", "progress-bar")
      progressBar.setAttribute("role", "progressbar")

      // Accessibility
      progressBar.setAttribute("aria-valuenow", 0)
      progressBar.setAttribute("aria-valuemin", 0)
      progressBar.setAttribute("aria-valuemax", 100)
      progress.appendChild(progressBar)

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
