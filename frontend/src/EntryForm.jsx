import { useState } from "react";

const EntryForm = ({existingEntry = {}, updateCallback}) => {
    const [rowNum, setRowNum] = useState(existingEntry.rowNum || '')
    const [colNum, setColNum] = useState(existingEntry.colNum || '')
    const [amount, setAmount] = useState(existingEntry.amount || '')

    const updating = Object.entries(existingEntry).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()
        const data = {
            rowNum, colNum, amount
        }
        const url = 'http://127.0.0.1:5000/' + (updating? `update_entries/${existingEntry.id}` : 'make_entries')
        const options = {
            method: updating? 'PATCH': 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }

        const response = await fetch(url, options)
        if (response.status != 201 && response.status != 200) {
            const data = await response.json()
            alert(data.message)
        }
        else {
            updateCallback()
        }
    }

    return <form onSubmit={onSubmit}>
        <div>
            <label htmlFor="rownum">Row Number</label>
            <input type="text" id="rownum" value={rowNum} onChange={(e) => setRowNum(e.target.value)} />
        </div>
        <div>
            <label htmlFor="colnum">Col Number</label>
            <input type="text" id="colnum" value={colNum} onChange={(e) => setColNum(e.target.value)} />
        </div>
        <div>
            <label htmlFor="amount">Amount</label>
            <input type="text" id="amount" value={amount} onChange={(e) => setAmount(e.target.value)} />
        </div>
        <button type="submit">{updating? 'Update Entry': 'Make Entry'}</button>
    </form>
}

export default EntryForm