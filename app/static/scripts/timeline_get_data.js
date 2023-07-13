function generateTemplate({name, created_at, content}) {

  const date = new Date(created_at)
  const day = date.getDate()
  const month = date.getMonth() + 1
  const year = date.getFullYear()

  return `
  <div class="post">
     <div class="post-left">
       <p class="content">${content}</p>
       <p class="name">${name}</p>
     </div>
     <div class="post-right">
       <p class="date">${month}/${day}/${year}</p>
     </div>
   </div>
 `
}

function getDataApi() {
  return fetch('/api/timeline_post', { method: 'GET' })
    .then((response) => response.json())
    .then((data) => {
      let posts = data.timeline_post
      const postSection = document.querySelector('.posts-section')
      postSection.innerHTML = ''

      posts.forEach((post) => {
        const postTemplate = generateTemplate(post)
        postSection.innerHTML += postTemplate
      })
    })
    .catch((error) => {
      console.error('Error:', error)
    })
}
