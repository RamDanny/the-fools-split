import React from "react";

const EntriesList = ({entries, updateEntry, updateCallback}) => {
    
    const onDelete = async (id) => {
        try {
            const options = {
                method: 'DELETE'
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_entries/${id}`, options)
            if (response.status == 200)
                updateCallback()
            else {
                console.error('Delete Failed!')
            }
        }
        catch (error) {
            alert(error)
        }
    }

    return <div>
        <h2>Entries</h2>
        <table>
            <thead>
                <tr>
                    <th>Row Num</th>
                    <th>Col Num</th>
                    <th>Amount</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {entries.map((entry) => (
                    <tr key={entry.id}>
                        <td>{entry.rowNum}</td>
                        <td>{entry.colNum}</td>
                        <td>{entry.amount}</td>
                        <td>
                            <button onClick={() => updateEntry(entry)}>Update</button>
                            <button onClick={() => onDelete(entry.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default EntriesList