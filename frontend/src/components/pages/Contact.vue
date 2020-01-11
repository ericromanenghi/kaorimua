<template>
    <TextPage title='Contact'>
        <p class='textpage__intro'>Love yourself as you are<br>and enjoy doing what you do</p>
        <p>My name is Kaori, a passionate beauty lover &amp; freelance makeup artist, hairstylist &amp; winner of the Talent Award of 2018 in The Netherlands. After finishing my Makeup Artist course at the Glamour Makeup I started freelancing straight away. </p>
        <ul class='contact'>
            <li>
                <span class='contact__name'>Phone</span>
                <span class='contact__value'>+31 614 502 921</span>
            </li>
            <li>
                <span class='contact__name'>E-mail</span>
                <span class='contact__value'><a href='#'>hello@kaorimua.nl</a></span>
            </li>
            <li>
                <span class='contact__name'>Instagram</span>
                <span class='contact__value'><a href='#'>@kaori_mua</a></span>
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

<style scoped lang='scss'>
@import './../../scss/variables.scss';

.contact {
    list-style: none;
    margin: 25px 0;
    padding: 0;
}
.contact li {
    font-size: .8em;
    margin-bottom: 15px;
}
.contact__name {
    display: block;
    margin-bottom: 5px;
}
.contact__value {
    font-size: 1.1em;
}
.contact a {
    color: $color-primary;
}
.contact a:hover {
    text-decoration: none;
}

@media screen and (min-width: 700px) {
    .contact li {
        align-items: center;
        display: flex;
        font-size: .9em;
    }
    .contact__name {
        margin-bottom: 0;
        width: 110px;
    }
    .contact__value {
        font-size: 1em;
    }
}
</style>
