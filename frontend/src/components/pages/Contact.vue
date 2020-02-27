<template>
    <TextPage title='Contact'>
        <p class='textpage__intro'>Do you want to get in touch with me?</p>
        <p>Feel free to contact me via Whatsapp or any of my social media profiles.</p>
        <ul class='contact'>
            <li>
                <span class='contact__name'>Phone</span>
                <span class='contact__value'>+31 614 802 365</span>
            </li>
            <li>
                <span class='contact__name'>E-mail</span>
                <span class='contact__value'><a href='#'>kaorimua@gmail.com</a></span>
            </li>
            <li>
                <span class='contact__name'>Instagram</span>
                <span class='contact__value'><a href='https://www.instagram.com/kaori_mua/' target="_blank">@kaori_mua</a></span>
            </li>
        </ul>
    </TextPage>
</template>

<script>
import TextPage from './../partials/TextPage'

export default {
    components: {
        TextPage,
    }
}
</script>

<style scoped lang='scss' src=@/scss/contact.scss></style>
