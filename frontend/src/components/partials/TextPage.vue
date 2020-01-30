<template>
    <div class='container'>
        <div class='textpage'>
            <div class='textpage__photo' :style='style'>
                <h1>{{ title }}</h1>
                <ul class='textpage__links'>
                    <li><a href='#'>Instagram</a></li>
                    <li><a href='#'>Facebook</a></li>
                    <li><a href='#'>Snapchat</a></li>
                </ul>
            </div>
            <div class='textpage__text'>
                <slot></slot>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: [ 'title' ],
    data: function () {
        return {
            style: `background-image: url(${process.env.BASE_URL}photos/kaori.jpg)`,
        }
    },
}
</script>

<style scoped lang='scss' src='@/scss/textpage.scss'></style>
