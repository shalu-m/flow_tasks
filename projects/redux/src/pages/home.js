import axios from "axios"
import { useEffect, useState } from "react"


export default function Home(){
    const [boox,setBooks]=useState([])
    const [insertlist,setlist]=useState({})

    useEffect(()=>{
        getBooks()
    },[])
    
    const getBooks=async()=>{
        const {data}=await axios.get('http:/localhost:39056/read')
        console.log(data)
        setBooks(data.data)
    }
    //insert 
    const insertBooks=async()=>{
        const insert_books=await axios.post('http/localhost:39056/create',JSON.stringify())
    }
    return(
       <div>
            <input type='text' onChange={(e)=>setlist({...insertlist,title:e.target.value})}/>
       </div>
    )
}