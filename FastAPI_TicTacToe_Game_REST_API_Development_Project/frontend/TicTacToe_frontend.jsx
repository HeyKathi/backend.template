import React from "react";
import { useEffect, useState } from "react";

function TicTacToe_frontend() {
    const [games, setGames] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch("http://127.0.0.1:8000")
            .then(res => res.json())
            .then(data =>
                setGames(data),
                setLoading(false)
            );
    }), [];

    const handleNewGameClick = () => {
        fetch("http://127.0.0.1:8000/new-game", {
            method: "POST"
        })
            .then(res => res.json())
            .then(data =>
                setGames(data)
            );
    }

    return (
        <div>
            <button onClick={handleNewGameClick}>Ein neues Game starten</button>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {games.map((game) => (
                        <li
                            key={game.id}
                            onClick={() => handleNewGameClick(game)}
                        >
                            Spiel #{game.id} - {game.status}
                        </li>
                    ))}
                </tbody>
            </table>
        </div>
    )
}