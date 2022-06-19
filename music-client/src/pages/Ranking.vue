<template>
    <div class="song-list">
        <ul class="song-list-header">
            <li v-for="(item,index) in ranking" :key="index" @click="handleChangeView(item.name)"
                :class="{active:item.name==activeName}">
                {{item.name}}
            </li>
        </ul>
        <album-content :songList="listOfSongs"> </album-content>
    </div>
</template>
<script>
import {mapGetters} from "vuex";
import AlbumContent from "../components/AlbumContent";
import {getAllSongList,getrankingListOfLikeStyle} from '../api/index';
import {mixin} from "../mixins";
import {ranking} from '../assets/data/songList';


export default {
    name: 'song-list',
    mixins: [mixin],
    components:{
        AlbumContent,
 
    },
    data(){
        return{
            songLists: [{"id": 11, "singer_id": 2, "name": "\u5468\u6770\u4f26-\u544a\u767d\u6c14\u7403", "introduction": "\u5e8a\u8fb9\u6545\u4e8b", "create_time": "2018-12-27T08:45:24Z", "update_time": "2018-12-27T08:45:24Z", "pic": "/img/songPic/gaobaiqiqui.jpg", "lyric": "[00:00.00] \u4f5c\u66f2 : \u5468\u6770\u4f26\n[00:01.00] \u4f5c\u8bcd : \u65b9\u6587\u5c71\n[00:32.840] \u585e\u7eb3\u6cb3\u7554 \u5de6\u5cb8\u7684\u5496\u5561\n[00:35.438] \u6211\u624b\u4e00\u676f \u54c1\u5c1d\u4f60\u7684\u7f8e\n[00:38.655] \u7559\u4e0b\u5507\u5370\u7684\u5634\n[00:43.273] \u82b1\u5e97\u73ab\u7470 \u540d\u5b57\u5199\u9519\u8c01\n[00:46.159] \u544a\u767d\u6c14\u7403 \u98ce\u5439\u5230\u5bf9\u8857\n[00:49.225] \u5fae\u7b11\u5728\u5929\u4e0a\u98de\n[00:53.503] \u4f60\u8bf4\u4f60\u6709\u70b9\u96be\u8ffd \u60f3\u8ba9\u6211\u77e5\u96be\u800c\u9000\n[00:58.374] \u793c\u7269\u4e0d\u9700\u6311\u6700\u8d35 \u53ea\u8981\u9999\u69ad\u7684\u843d\u53f6\n[01:04.141] \u5594 \u8425\u9020\u6d6a\u6f2b\u7684\u7ea6\u4f1a \u4e0d\u5bb3\u6015\u641e\u7838\u4e00\u5207\n[01:09.205] \u62e5\u6709\u4f60\u5c31\u62e5\u6709 \u5168\u4e16\u754c\n[01:14.289] \u4eb2\u7231\u7684 \u7231\u4e0a\u4f60 \u4ece\u90a3\u5929\u8d77\n[01:20.520] \u751c\u871c\u7684\u5f88\u8f7b\u6613\n[01:25.040] \u4eb2\u7231\u7684 \u522b\u4efb\u6027 \u4f60\u7684\u773c\u775b\n[01:31.189] \u5728\u8bf4\u6211\u613f\u610f\n[01:57.772] \u585e\u7eb3\u6cb3\u7554 \u5de6\u5cb8\u7684\u5496\u5561\n[02:00.373] \u6211\u624b\u4e00\u676f \u54c1\u5c1d\u4f60\u7684\u7f8e\n[02:03.323] \u7559\u4e0b\u5507\u5370\u7684\u5634\n[02:08.304] \u82b1\u5e97\u73ab\u7470 \u540d\u5b57\u5199\u9519\u8c01\n[02:10.954] \u544a\u767d\u6c14\u7403 \u98ce\u5439\u5230\u5bf9\u8857\n[02:14.125] \u5fae\u7b11\u5728\u5929\u4e0a\u98de\n[02:18.302] \u4f60\u8bf4\u4f60\u6709\u70b9\u96be\u8ffd \u60f3\u8ba9\u6211\u77e5\u96be\u800c\u9000\n[02:23.187] \u793c\u7269\u4e0d\u9700\u6311\u6700\u8d35 \u53ea\u8981\u9999\u69ad\u7684\u843d\u53f6\n[02:28.500] \u5594 \u8425\u9020\u6d6a\u6f2b\u7684\u7ea6\u4f1a \u4e0d\u5bb3\u6015\u641e\u7838\u4e00\u5207\n[02:33.745] \u62e5\u6709\u4f60\u5c31\u62e5\u6709 \u5168\u4e16\u754c\n[02:39.115] \u4eb2\u7231\u7684 \u7231\u4e0a\u4f60 \u4ece\u90a3\u5929\u8d77\n[02:45.012] \u751c\u871c\u7684\u5f88\u8f7b\u6613\n[02:49.827] \u4eb2\u7231\u7684 \u522b\u4efb\u6027 \u4f60\u7684\u773c\u775b\n[02:55.829] \u5728\u8bf4\u6211\u613f\u610f\n[03:00.627] \u4eb2\u7231\u7684 \u7231\u4e0a\u4f60 \u604b\u7231\u65e5\u8bb0\n[03:06.656] \u98d8\u9999\u6c34\u7684\u56de\u5fc6\n[03:11.150] \u4e00\u6574\u74f6 \u7684\u68a6\u5883 \u5168\u90fd\u6709\u4f60\n[03:17.249] \u6405\u62cc\u5728\u4e00\u8d77\n[03:21.813] \u4eb2\u7231\u7684\u522b\u4efb\u6027 \u4f60\u7684\u773c\u775b\n[03:31.562] \u5728\u8bf4\u6211\u613f\u610f", "url": "/song/\u5468\u6770\u4f26-\u544a\u767d\u6c14\u7403.mp3"}],
            currentPage: 1,      //当前页，默认第一页
            ranking: [],           //风格
            activeName: '飙升榜'    //当前风格
        }
    },
    computed:{
       ...mapGetters([
            'listOfSongs',      //当前播放列表
            'tempList',         //当前歌单对象
            'loginIn',          //用户是否已登录
            'userId',           //当前登录用户id
        ])
    },
    mounted(){
        this.ranking = ranking;
        this.getSongList();
    },

    methods:{
        getSongList(){            
           getrankingListOfLikeStyle('飙升榜')
                .then(res =>{
                    this.currentPage = 1;
                    this.songLists = res
                     this.$store.commit('setListOfSongs',this.songLists);
                })           
        },
        //获取当前页
        handleCurrentChange(val){
            this.currentPage = val;
        },
        //根据style显示对应的歌单
        handleChangeView(name){
            this.activeName = name;
            this.albumDatas = [];
            if(name == '飙升榜'){
                this.goSongListOfStyle(name)
            }else{
                console.log(name)
                this.goSongListOfStyle(name)
            }
        },
        //根据style查询对应的歌单
        goSongListOfStyle(style){
            getrankingListOfLikeStyle(style)
                .then(res =>{
                        this.currentPage = 1;
                        this.albumDatas = res;
                        this.songLists = res;
                        console.log(this.songLists);
                         this.$store.commit('setListOfSongs',this.songLists);
                    }) 
        },

    }
}


</script>

<style lang="scss" scoped>
@import '../assets/css/song-list.scss';
</style>
