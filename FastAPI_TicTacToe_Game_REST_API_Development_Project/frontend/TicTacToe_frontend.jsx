import React, { useEffect, useState } from "react";

function TicTacToe_frontend() {
    const [games, setGames] = useState([]);
    const [selectedGame, setSelectedGame] = useState(null);
    const [loading, setLoading] = useState(true);

    const API_BASE = "http://127.0.0.1:8000";

    useEffect(() => {
        fetchGames();
    }, []);

    const fetchGames = async () => {
        try {
            const res = await fetch(`${API_BASE}/games`);
            const data = await res.json();
            setGames(data);
            setLoading(false);
        } catch (error) {
            console.error("Error fetching games:", error);
            setLoading(false);
        }
    };

    const createNewGame = async () => {
        try {
            const res = await fetch(`${API_BASE}/games`, {
                method: "POST",
            });
            const newGame = await res.json();
            setGames([...games, newGame]);
            setSelectedGame(newGame);
        } catch (error) {
            console.error("Error creating game:", error);
        }
    };

    const selectGame = async (gameId) => {
        try {
            const res = await fetch(`${API_BASE}/games/${gameId}`);
            const game = await res.json();
            setSelectedGame(game);
        } catch (error) {
            console.error("Error fetching game:", error);
        }
    };

    const makeMove = async (position) => {
        if (!selectedGame || selectedGame.status !== "ongoing") return;

        try {
            const res = await fetch(`${API_BASE}/games/${selectedGame.id}/move/${position + 1}`, {
                method: "PUT",
            });
            if (res.ok) {
                const updatedGame = await res.json();
                setSelectedGame(updatedGame);
                // Update in games list
                setGames(games.map(g => g.id === updatedGame.id ? updatedGame : g));
            } else {
                const error = await res.json();
                alert(error.detail);
            }
        } catch (error) {
            console.error("Error making move:", error);
        }
    };

    const renderBoard = () => {
        if (!selectedGame) return null;

        const board = selectedGame.board.split("");
        return (
            <div className="game-board">
                {board.map((cell, index) => (
                    <div
                        key={index}
                        className="cell"
                        onClick={() => makeMove(index)}
                    >
                        {cell === "-" ? "" : cell}
                    </div>
                ))}
            </div>
        );
    };

    const getStatusMessage = () => {
        if (!selectedGame) return "";
        if (selectedGame.status === "ongoing") {
            return `Spieler ${selectedGame.current_player} ist am Zug`;
        } else if (selectedGame.status.includes("_wins")) {
            const winner = selectedGame.status.split("_")[0];
            return `Spieler ${winner} hat gewonnen!`;
        } else if (selectedGame.status === "draw") {
            return "Unentschieden!";
        }
        return selectedGame.status;
    };

    if (loading) {
        return <div>Lade Spiele...</div>;
    }

    return (
        <div>
            <button className="new-game-btn" onClick={createNewGame}>
                Neues Spiel starten
            </button>

            <div className="game-list">
                <h2>Verfügbare Spiele</h2>
                {games.map((game) => (
                    <div
                        key={game.id}
                        className="game-item"
                        onClick={() => selectGame(game.id)}
                    >
                        Spiel #{game.id} - {game.status}
                    </div>
                ))}
            </div>

            {selectedGame && (
                <div>
                    <h2>Spiel #{selectedGame.id}</h2>
                    {renderBoard()}
                    <div className="status">{getStatusMessage()}</div>
                </div>
            )}
        </div>
    );
}

export default TicTacToe_frontend;