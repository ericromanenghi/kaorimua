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

<style scoped lang='scss'>
@import './../../scss/variables.scss';

.textpage {
    padding: 10px;
}
.textpage__photo {
    background-color: $color-secondary;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    display: block;
    padding: 110px 20px 30px;
}
.textpage__photo h1 {
    color: #fff;
    font-size: 1.7em;
    margin: 0 0 10px;
    text-align: center;
}
.textpage__links {
    list-style: none;
    margin: 0;
    padding: 0;
    text-align: center;
}
.textpage__links li {
    display: inline-block;
    font-size: .8em;
}
.textpage__links a {
    color: #fff;
    display: inline-block;
    padding: 5px;
}
.textpage__links a:hover {
    text-decoration: none;
}
.textpage__text {
    padding: 40px 20px;
}
.textpage__text .textpage__intro {
    font-size: 1.3em;
    font-style: italic;
    margin: 0 0 20px;
}
.textpage__text p {
    font-size: .8em;
    line-height: 1.7;
    margin: 0 0 15px;
}

@media screen and (min-width: 990px) {
    .textpage {
        align-items: center;
        display: flex;
        min-height: 100vh;
        position: relative;
    }
    .textpage__text {
        max-width: 500px;
        padding: 40px 30px;
        width: 50%;
    }
    .textpage__text p {
        font-size: .9em;
    }
    .textpage__photo {
        align-items: center;
        display: flex;
        flex-direction: column;
        height: calc(100vh - 30px);
        justify-content: center;
        right: 15px;
        padding: 20px;
        position: fixed;
        top: 15px;
        width: calc(50% - 150px);
    }
    .textpage__photo h1 {
        font-size: 2em;
    }
}

@media screen and (min-width: 1200px) {
    .textpage__photo {
        width: 450px;
    }
}
</style>
