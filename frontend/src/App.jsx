import { useEffect, useState } from 'react'
import EntriesList from './EntriesList'
import EntryForm from './EntryForm'
import './App.css'

function App() {
  const [entries, setEntries] = useState([{'rowNum': 0, 'colNum': 0, 'amount': 10, 'id':1}])
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentEntry, setCurrentEntry] = useState({})

  useEffect(() => {
    getEntries()
  }, [])

  const getEntries = async () => {
    const response = await fetch('http://127.0.0.1:5000/entries')
    const data = await response.json()
    setEntries(data.entries)
    console.log(data.entries)
  }

  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentEntry({})
  }

  const openCreateModal = () => {
    if (!isModalOpen)
      setIsModalOpen(true)
  }

  const openEditModal = (entry) => {
    if (isModalOpen) return
    setCurrentEntry(entry)
    setIsModalOpen(true)
  }

  const onUpdate = () => {
    closeModal()
    getEntries()
  }

  return (
    <>
      <EntriesList entries={entries} updateEntry={openEditModal} updateCallback={onUpdate}/>
      <button onClick={openCreateModal}>Make Entry</button>
      {
        isModalOpen && <div className='modal'>
          <div className='modal-content'>
            <span className='close' onClick={closeModal}>&times;</span>
            <EntryForm existingEntry={currentEntry} updateCallback={onUpdate}/>
          </div>
        </div>
      }
    </>
  )
}

export default App
