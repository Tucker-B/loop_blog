let post_content_p_elements = document.querySelectorAll('.post_content p');


post_content_p_elements.forEach((p_element) => {
    let p_text = p_element.innerText;
    if (p_text.length > 20) {
        p_element.innerText = p_text.substr(0, 20) + "...";
    }
})
